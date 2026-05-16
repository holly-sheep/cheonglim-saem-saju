#!/usr/bin/env python3
"""Send owner-requested disregard notices for the accidental outreach emails."""

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
class Retraction:
    identifier: str
    target: str
    to_email: str
    original_subject: str


RETRACTIONS: list[Retraction] = [
    Retraction("kdramadiary-001", "KDRAMADIARY", "kdramadiary.official@gmail.com", "Korean Four Pillars explainer for K-culture readers"),
    Retraction("kpop-kollective-001", "Kpop Kollective", "kpkgenadm@gmail.com", "Korean Saju / Four Pillars explainer for Hallyu readers"),
    Retraction("kdramastars-001", "KDramaStars", "info@kdramastars.com", "Korean Four Pillars reading angle for global K-culture fans"),
]


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


def build_message(retraction: Retraction, from_email: str) -> EmailMessage:
    message = EmailMessage()
    message["From"] = f"Cheonglim Saem <{from_email}>"
    message["To"] = retraction.to_email
    message["Reply-To"] = from_email
    message["Subject"] = f"Please disregard previous email: {retraction.original_subject}"
    message.set_content(
        f"""Hi {retraction.target} team,

Please disregard the previous email from Cheonglim Saem with this subject:

{retraction.original_subject}

It was sent by an AI assistant before final human approval. Please ignore the message and do not take any action on it.

Sorry for the inconvenience.

Cheonglim Saem
aideseobot@gmail.com
"""
    )
    return message


def send_retractions(env: dict[str, str], dry_run: bool) -> None:
    from_email = env.get("SAJU_FROM_EMAIL") or env["SAJU_SMTP_USER"]
    if dry_run:
        for retraction in RETRACTIONS:
            print(f"dry-run: would send retraction for {retraction.identifier} to {retraction.to_email}")
        return
    with smtplib.SMTP_SSL(env["SAJU_SMTP_HOST"], int(env.get("SAJU_SMTP_PORT", "465"))) as smtp:
        smtp.login(env["SAJU_SMTP_USER"], env["SAJU_SMTP_PASSWORD"])
        for retraction in RETRACTIONS:
            smtp.send_message(build_message(retraction, from_email))
            print(f"retraction sent: {retraction.identifier} to {retraction.to_email}")


def update_logs(sent_at: str) -> None:
    queue_fields, queue_rows = read_rows(QUEUE)
    tracker_fields, tracker_rows = read_rows(TRACKER)
    evidence_fields, evidence_rows = read_rows(EVIDENCE)
    by_target = {item.target: item for item in RETRACTIONS}

    for row in queue_rows:
        item = by_target.get(row.get("target", ""))
        if not item:
            continue
        row["status"] = "retraction_sent"
        row["response_at"] = sent_at
        row["next_step"] = "Do not contact again unless owner explicitly approves"

    for row in tracker_rows:
        for item in RETRACTIONS:
            if item.target in row.get("asset_or_post", ""):
                row["status"] = "retraction_sent"
                row["next_action"] = "Do not contact again unless owner explicitly approves"

    existing_ids = {row.get("identifier") for row in evidence_rows}
    for item in RETRACTIONS:
        identifier = f"{item.identifier}-retraction"
        if identifier in existing_ids:
            continue
        evidence_rows.append(
            {
                "timestamp": sent_at,
                "type": "outreach_retraction_sent",
                "source": "smtp",
                "identifier": identifier,
                "evidence": f"sent disregard notice to {item.to_email}",
                "notes": "owner requested correction: previous AI-sent outreach should be ignored",
            }
        )

    write_rows(QUEUE, queue_fields, queue_rows)
    write_rows(TRACKER, tracker_fields, tracker_rows)
    write_rows(EVIDENCE, evidence_fields, evidence_rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--confirm-send", action="store_true")
    parser.add_argument("--approval-note", default="")
    args = parser.parse_args()

    if not args.dry_run and (not args.confirm_send or args.approval_note != "USER_REQUESTED_RETRACTION_EMAIL"):
        print(
            "blocked: real retraction email requires --confirm-send "
            "--approval-note USER_REQUESTED_RETRACTION_EMAIL"
        )
        return 2

    env = os.environ | load_env(args.env_file)
    send_retractions(env, args.dry_run)
    if not args.dry_run:
        update_logs(datetime.now(SEOUL).isoformat(timespec="seconds"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
