# Conversion Evidence Ledger

Last updated: 2026-05-16T14:22:52+09:00

This file separates actual evidence from planned promotion. Do not count a channel as working until an external artifact proves it.

## Current Evidence Baseline

GitHub repo traffic snapshot, checked with `gh api repos/holly-sheep/cheonglim-saem-saju/traffic/views`:

- 2026-05-13: 7 views, 1 unique
- 2026-05-14: 20 views, 1 unique
- 14-day total at check time: 27 views, 1 unique

This is weak evidence because it is repository traffic, not confirmed customer site traffic. Treat it as a baseline only, not as qualified visits.

## Evidence Rules

- Qualified visit evidence: platform analytics screenshot, GitHub Pages/custom domain analytics if available, or a UTM-tagged lead/order email that proves the visitor came from a campaign URL.
- Free preview lead evidence: an email body containing `lead_type: free_mini_preview_followup` plus `utm_source`, `utm_campaign`, and ideally `utm_content`.
- Creator review lead evidence: an email body containing `lead_type: free_vip_review_application` plus source fields.
- Paid order evidence: USDT-TRC20 payment receipt, wallet transaction hash, or order email body from `intake.html` that can be matched to a payment.
- Test clicks, local screenshots, curl requests, and repo views do not count as qualified visits unless a real external user or platform analytics source is attached.

## Daily Manual Check

1. Open the posted platform and capture the post URL or screenshot.
2. Update `marketing/campaign-tracker.csv` with `date`, `status`, and `evidence_url_or_file`.
3. Check email for `lead_type:` lines and copy the UTM source fields into the tracker.
4. Check the USDT wallet for matching payment receipts before counting paid orders.
5. Append hard evidence to `marketing/evidence-log.csv`.

## Outbound Safety

Do not send emails, DMs, contact-form submissions, or follow-ups unless the owner explicitly approves that exact outbound batch. Public posts made manually by the owner should be logged as `post_published`, not `outreach_sent`.
