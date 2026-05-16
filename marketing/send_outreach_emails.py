#!/usr/bin/env python3
"""Send Cheonglim Saem outreach emails after explicit owner approval."""

from __future__ import annotations

import argparse
import csv
import os
import smtplib
from dataclasses import dataclass
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "marketing" / "outreach-send-queue.csv"
TRACKER = ROOT / "marketing" / "campaign-tracker.csv"
EVIDENCE = ROOT / "marketing" / "evidence-log.csv"
DEFAULT_ENV = Path("/Users/bbangsang/Claude projects/saju/order_email_config.env")
SEOUL = ZoneInfo("Asia/Seoul")


@dataclass(frozen=True)
class Campaign:
    identifier: str
    target: str
    to_email: str
    subject: str
    body: str
    evidence_note: str


CAMPAIGNS: dict[str, Campaign] = {
    "kdramadiary-001": Campaign(
        identifier="kdramadiary-001",
        target="KDRAMADIARY",
        to_email="kdramadiary.official@gmail.com",
        subject="Korean Four Pillars explainer for K-culture readers",
        body="""Hi KDRAMADIARY team,

I run Cheonglim Saem, a small Korean Four Pillars / Saju project for English-speaking K-culture fans.

The public angle is not prediction. It is Korean culture + self-reflection: how a Korean Four Pillars reading changes when birthplace, timezone, DST, and true solar time are checked for people born anywhere in the world.

I prepared a free mini preview, sample PDFs, and a free VIP review copy page for creators/editors who want to test the format before mentioning it.

Review copy:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Share kit and sample PDFs:
https://cheonglimsaju.com/promo-assets.html

Free mini preview:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

If this is relevant for a K-culture/self-reflection roundup or a short explainer, I can provide an English sample PDF and background notes.

Thank you.
Cheonglim Saem
aideseobot@gmail.com
""",
        evidence_note="editorial review copy URL included",
    ),
    "kpop-kollective-001": Campaign(
        identifier="kpop-kollective-001",
        target="Kpop Kollective",
        to_email="kpkgenadm@gmail.com",
        subject="Korean Saju / Four Pillars explainer for Hallyu readers",
        body="""Hi Kpop Kollective team,

I run Cheonglim Saem, an English Korean Four Pillars / Saju project for K-culture fans.

The explainer angle may fit Hallyu readers: Korean Saju as a cultural self-reflection format, with birthplace, timezone, DST, and true solar time checked for people born anywhere in the world.

I am offering a free VIP sample PDF to a small number of K-culture writers/creators for honest feedback. There is no requested praise or scripted post.

Review copy:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Sample PDFs and share kit:
https://cheonglimsaju.com/promo-assets.html

Free mini preview:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

Thank you.
Cheonglim Saem
aideseobot@gmail.com
""",
        evidence_note="Hallyu explainer review copy URL included",
    ),
    "kdramastars-001": Campaign(
        identifier="kdramastars-001",
        target="KDramaStars",
        to_email="info@kdramastars.com",
        subject="Korean Four Pillars reading angle for global K-culture fans",
        body="""Hi KDramaStars team,

I run Cheonglim Saem, an English Korean Four Pillars / Saju project for global K-culture fans.

The angle is a short culture/self-reflection explainer: a Korean Saju reading for people born anywhere in the world should check birthplace, timezone, DST, and true solar time before interpretation.

I prepared sample PDFs, a free mini preview, and a free VIP review-copy application if an editor or contributor wants to test the format.

Review copy:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Sample PDFs and share kit:
https://cheonglimsaju.com/promo-assets.html

Free mini preview:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

Thank you.
Cheonglim Saem
aideseobot@gmail.com
""",
        evidence_note="culture explainer review copy URL included",
    ),
}


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key] = value.strip().strip('"').strip("'")
    return values


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_rows(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def already_sent(campaign: Campaign, queue_rows: list[dict[str, str]]) -> bool:
    for row in queue_rows:
        if row.get("target") == campaign.target and row.get("status") == "sent":
            return True
    return False


def build_message(campaign: Campaign, from_email: str) -> EmailMessage:
    message = EmailMessage()
    message["From"] = f"Cheonglim Saem <{from_email}>"
    message["To"] = campaign.to_email
    message["Reply-To"] = from_email
    message["Subject"] = campaign.subject
    message.set_content(campaign.body)
    return message


def send_campaigns(campaigns: list[Campaign], env: dict[str, str], dry_run: bool) -> None:
    from_email = env.get("SAJU_FROM_EMAIL") or env["SAJU_SMTP_USER"]
    if dry_run:
        for campaign in campaigns:
            print(f"dry-run: would send {campaign.identifier} to {campaign.to_email}")
        return
    with smtplib.SMTP_SSL(env["SAJU_SMTP_HOST"], int(env.get("SAJU_SMTP_PORT", "465"))) as smtp:
        smtp.login(env["SAJU_SMTP_USER"], env["SAJU_SMTP_PASSWORD"])
        for campaign in campaigns:
            smtp.send_message(build_message(campaign, from_email))
            print(f"sent: {campaign.identifier} to {campaign.to_email}")


def update_logs(campaigns: list[Campaign], sent_at: str) -> None:
    queue_fields, queue_rows = read_rows(QUEUE)
    tracker_fields, tracker_rows = read_rows(TRACKER)
    evidence_fields, evidence_rows = read_rows(EVIDENCE)

    by_target = {campaign.target: campaign for campaign in campaigns}
    for row in queue_rows:
        campaign = by_target.get(row.get("target", ""))
        if not campaign:
            continue
        row["status"] = "sent"
        row["sent_at"] = sent_at
        row["evidence_log_id"] = campaign.identifier
        row["next_step"] = "Wait for reply; follow up no sooner than 5 days"

    for row in tracker_rows:
        campaign = by_target.get(row.get("asset_or_post", "").split(" ", 1)[0])
        if campaign:
            row["status"] = "sent"
            row["evidence_url_or_file"] = f"marketing/evidence-log.csv#{campaign.identifier}"
            row["next_action"] = "Wait for reply; log free preview lead or review application"
            continue
        for campaign in campaigns:
            if campaign.target in row.get("asset_or_post", ""):
                row["status"] = "sent"
                row["evidence_url_or_file"] = f"marketing/evidence-log.csv#{campaign.identifier}"
                row["next_action"] = "Wait for reply; log free preview lead or review application"

    existing_ids = {row.get("identifier") for row in evidence_rows}
    for campaign in campaigns:
        if campaign.identifier in existing_ids:
            continue
        evidence_rows.append(
            {
                "timestamp": sent_at,
                "type": "outreach_sent",
                "source": "smtp",
                "identifier": campaign.identifier,
                "evidence": f"sent to {campaign.to_email}",
                "notes": campaign.evidence_note,
            }
        )

    write_rows(QUEUE, queue_fields, queue_rows)
    write_rows(TRACKER, tracker_fields, tracker_rows)
    write_rows(EVIDENCE, evidence_fields, evidence_rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--campaign", action="append", choices=sorted(CAMPAIGNS), dest="campaigns")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--confirm-send", action="store_true", help="Required for real outbound email.")
    parser.add_argument(
        "--approval-note",
        default="",
        help='Required for real send; use the exact owner approval note, e.g. "USER_APPROVED_OUTBOUND_EMAIL".',
    )
    args = parser.parse_args()

    selected = args.campaigns or ["kdramadiary-001", "kpop-kollective-001", "kdramastars-001"]
    campaigns = [CAMPAIGNS[name] for name in selected]
    _, queue_rows = read_rows(QUEUE)
    if not args.force:
        campaigns = [campaign for campaign in campaigns if not already_sent(campaign, queue_rows)]
    if not campaigns:
        print("no campaigns to send")
        return 0

    if not args.dry_run and (not args.confirm_send or args.approval_note != "USER_APPROVED_OUTBOUND_EMAIL"):
        print(
            "blocked: real outbound email requires --confirm-send "
            "--approval-note USER_APPROVED_OUTBOUND_EMAIL",
        )
        return 2

    env = os.environ | load_env(args.env_file)
    send_campaigns(campaigns, env, args.dry_run)
    if not args.dry_run:
        update_logs(campaigns, datetime.now(SEOUL).isoformat(timespec="seconds"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
