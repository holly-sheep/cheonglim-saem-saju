# IndexNow Submission

Status: submitted

Use this only for Cheonglim-owned URLs. The key file is public at:

https://cheonglimsaju.com/cheonglim-saju-indexnow-20260516-7ab7.txt

Submission script:

```sh
scripts/submit-indexnow.sh
```

URLs in the first batch:

- https://cheonglimsaju.com/
- https://cheonglimsaju.com/bio.html
- https://cheonglimsaju.com/start.html
- https://cheonglimsaju.com/free-korean-saju-reading.html
- https://cheonglimsaju.com/overseas-birth-saju.html
- https://cheonglimsaju.com/saju-in-english.html
- https://cheonglimsaju.com/korean-saju-reading-online.html
- https://cheonglimsaju.com/true-solar-time-saju.html
- https://cheonglimsaju.com/saju-without-birth-time.html
- https://cheonglimsaju.com/korean-birthday-reading.html
- https://cheonglimsaju.com/korean-compatibility-reading.html
- https://cheonglimsaju.com/kfortune-2026-2027-timing.html
- https://cheonglimsaju.com/basic-korean-saju-report.html
- https://cheonglimsaju.com/free-vip-review.html
- https://cheonglimsaju.com/trust-policies.html
- https://cheonglimsaju.com/promo-assets.html

Evidence rule: an HTTP 200 or 202 from the IndexNow endpoint proves URL submission was received. It does not prove search ranking, qualified visits, preview leads, or paid orders.

## Submission Evidence

- 2026-05-16T16:18:30+09:00: `scripts/submit-indexnow.sh` returned `HTTP/2 202` from `https://api.indexnow.org/indexnow`.
- Live key file check before submission: `https://cheonglimsaju.com/cheonglim-saju-indexnow-20260516-7ab7.txt` returned HTTP 200 and the expected key text.
- 2026-05-16T16:28:50+09:00: after adding `saju-in-english.html`, `scripts/submit-indexnow.sh` returned `HTTP/2 200` from `https://api.indexnow.org/indexnow`.
- 2026-05-16T16:41:54+09:00: after adding `free-korean-saju-reading.html`, `scripts/submit-indexnow.sh` returned `HTTP/2 200` from `https://api.indexnow.org/indexnow`.
- 2026-05-16T16:58:08+09:00: after verifying the birthday, compatibility, and 2026/2027 timing angle pages live, `scripts/submit-indexnow.sh` returned `HTTP/2 200` from `https://api.indexnow.org/indexnow`.
