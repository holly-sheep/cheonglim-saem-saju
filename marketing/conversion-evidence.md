# Conversion Evidence Ledger

Last updated: 2026-05-16T15:35:36+09:00

This file separates actual evidence from planned promotion. Do not count a channel as working until an external artifact proves it.

## Current Evidence Baseline

GitHub repo traffic snapshot, checked with `gh api repos/holly-sheep/cheonglim-saem-saju/traffic/views`:

- 2026-05-13: 7 views, 1 unique
- 2026-05-14: 20 views, 1 unique
- 14-day total at check time: 27 views, 1 unique

This is weak evidence because it is repository traffic, not confirmed customer site traffic. Treat it as a baseline only, not as qualified visits.

TRON USDT wallet snapshot, checked with Tronscan token transfer API for `TPinvSovyuBHTVK1Kd6bUYYESMoSBxjgjJ`:

- Latest USDT transfer involving the wallet: 2025-10-31T01:06:06Z, outbound 201.411351 USDT, tx `114b9e9ef71dcb993f16d46e2e47ff70c80b37dab69a3c353308d9d739336a0d`
- Latest inbound USDT transfer: 2025-10-31T00:55:42Z, inbound 201.411351 USDT, tx `9cd3f43612033afcb46655003494cd78ea1b287e83e452f37b9a40e0f10bb70e`
- No inbound transfers in the checked latest 20 token transfers matched the package prices `9`, `19`, or `39` USDT.

This proves no current paid-order evidence was found in the public wallet check. It does not prove there were no payments to a different address or unreconciled checkout path.

Rechecked on 2026-05-16T15:35:36+09:00 after the homepage deployment. The latest 20 USDT transfer rows still showed no inbound `9`, `19`, or `39` USDT package-price match.

Rechecked on 2026-05-16T16:22:06+09:00 with TronGrid TRC20 transaction API for the same wallet and USDT contract. The latest 20 rows still showed no inbound `9`, `19`, or `39` USDT package-price match. The latest transfer was still tx `114b9e9ef71dcb993f16d46e2e47ff70c80b37dab69a3c353308d9d739336a0d`, outbound `201.411351` USDT at 2025-10-31T01:06:06Z.

Rechecked on 2026-05-16T16:34:46+09:00 after the checkout Gmail fallback deployment. The latest 20 TronGrid USDT TRC20 rows still showed no inbound `9`, `19`, or `39` USDT package-price match.

Rechecked on 2026-05-16T16:58:59+09:00 after the SEO/social angle page live checks and IndexNow resubmission. The latest 5 TronGrid USDT TRC20 rows still showed no inbound `9`, `19`, or `39` USDT package-price match. The latest transfer was still tx `114b9e9ef71dcb993f16d46e2e47ff70c80b37dab69a3c353308d9d739336a0d`, outbound `201.411351` USDT at 2025-10-31T01:06:06Z.

Rechecked on 2026-05-16T17:04:32+09:00 after adding the trust and policies page. The latest 5 TronGrid USDT TRC20 rows still showed no inbound `9`, `19`, or `39` USDT package-price match. The latest transfer was still tx `114b9e9ef71dcb993f16d46e2e47ff70c80b37dab69a3c353308d9d739336a0d`, outbound `201.411351` USDT at 2025-10-31T01:06:06Z.

Rechecked on 2026-05-16T17:09:04+09:00 after adding the package reservation intent CTA. The latest 5 TronGrid USDT TRC20 rows still showed no inbound `9`, `19`, or `39` USDT package-price match. The latest transfer was still tx `114b9e9ef71dcb993f16d46e2e47ff70c80b37dab69a3c353308d9d739336a0d`, outbound `201.411351` USDT at 2025-10-31T01:06:06Z.

## Evidence Rules

- Qualified visit evidence: platform analytics screenshot, GitHub Pages/custom domain analytics if available, or a UTM-tagged lead/order email that proves the visitor came from a campaign URL.
- Free preview lead evidence: an email body containing `lead_type: free_mini_preview_followup` or `lead_type: free_mini_preview_request` plus `utm_source`, `utm_campaign`, and ideally `utm_content`. The preview result and free preview page offer mailto, copy text, and Gmail draft fallback; only a sent email counts as a lead.
- Creator review lead evidence: an email body containing `lead_type: free_vip_review_application` plus source fields.
- Payment-intent lead evidence: an email body containing `lead_type: payment_question_or_intent` or `lead_type: order_reservation_intent`, selected `tier`, `amount`, and UTM fields. Count this separately from paid orders because it proves checkout or reservation intent, not completed payment.
- Paid order evidence: USDT-TRC20 payment receipt, wallet transaction hash, or order email body from `intake.html` that can be matched to a payment.
- Test clicks, local screenshots, curl requests, and repo views do not count as qualified visits unless a real external user or platform analytics source is attached.

## Daily Manual Check

1. Open the posted platform and capture the post URL or screenshot.
2. Update `marketing/campaign-tracker.csv` with `date`, `status`, and `evidence_url_or_file`.
3. Check email for `lead_type:` lines and copy the UTM source fields into the tracker.
4. Count `payment_question_or_intent` or `order_reservation_intent` as payment-intent lead only, then follow up manually before counting a paid order.
5. Check the USDT wallet for matching payment receipts before counting paid orders.
6. Append hard evidence to `marketing/evidence-log.csv`.

## Outbound Safety

Do not send emails, DMs, contact-form submissions, or follow-ups unless the owner explicitly approves that exact outbound batch. Public posts made manually by the owner should be logged as `post_published`, not `outreach_sent`.
