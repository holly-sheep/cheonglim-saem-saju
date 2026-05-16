# Send-Ready Outreach Queue

Last checked: 2026-05-16

Use this file to send the first outreach wave. After sending, update `marketing/outreach-send-queue.csv`, `marketing/campaign-tracker.csv`, and `marketing/evidence-log.csv`.

Outbound rule: do not send additional emails, DMs, contact-form messages, or follow-ups unless the owner explicitly says to send. The helper script blocks real outbound email unless both `--confirm-send` and `--approval-note USER_APPROVED_OUTBOUND_EMAIL` are present.

## 1. piecesofminty

Source: https://piecesofminty.carrd.co/

Observed public contact evidence:

- The Carrd describes Minty as a Thai-American blogger and long-time K-drama/K-pop fan.
- The page has public contact/email/social links. Use the public page route instead of guessing an address.

Short DM/contact form pitch:

```text
Hi Minty,

I run Cheonglim Saem, an English K-fortune project that explains Korean Saju/Four Pillars for people born anywhere in the world.

The angle is Korean culture + self-reflection, not hard prediction. The report checks birthplace, timezone, DST, and true solar time before interpretation, which is especially relevant for overseas-born K-culture fans.

I am offering a free VIP PDF for honest feedback from a small number of K-culture creators. No scripted praise; private feedback is fine.

Review application:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=dm&utm_campaign=kfortune_launch

Share kit and sample PDFs:
https://cheonglimsaju.com/promo-assets.html
```

Evidence log after routing:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,contact_page,piecesofminty-001,sent via public Carrd contact/social route,free VIP review application URL included
```

## 2. KDRAMADIARY

Source: https://kdramadiary.com/about-kdramadiary/

Observed public contact evidence:

- The about page describes KDRAMADIARY as a digital publication covering K-dramas, Asian dramas, concerts, Korea travel, and K-drama locations.
- The page lists media partnership emails, including `kdramadiary.official@gmail.com`.

To:

kdramadiary.official@gmail.com

Subject:

Korean Four Pillars explainer for K-culture readers

Body:

```text
Hi KDRAMADIARY team,

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
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,kdramadiary-001,sent to kdramadiary.official@gmail.com,editorial review copy URL included
```

## 3. Kpop Kollective

Source: https://kpopkollective.com/contact-us/

Observed public contact evidence:

- The contact page frames the site as Hallyu/K-pop focused and lists `kpkgenadm@gmail.com`.

To:

kpkgenadm@gmail.com

Subject:

Korean Saju / Four Pillars explainer for Hallyu readers

Body:

```text
Hi Kpop Kollective team,

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
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,kpop-kollective-001,sent to kpkgenadm@gmail.com,Hallyu explainer review copy URL included
```

## 4. KDramaStars

Source: https://www.kdramastars.com/contact-us

Observed public contact evidence:

- The public contact page lists `info@kdramastars.com` for general inquiries.

To:

info@kdramastars.com

Subject:

Korean Four Pillars reading angle for global K-culture fans

Body:

```text
Hi KDramaStars team,

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
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,kdramastars-001,sent to info@kdramastars.com,culture explainer review copy URL included
```

## 5. Talie Tarot

Source: https://linktr.ee/talietarot

Observed public contact evidence:

- The Linktree page lists `talietarot@gmail.com` as a business inquiry email.
- Fit: tarot audience, fortune/self-reflection category, Korean-language creator.

To:

talietarot@gmail.com

Subject:

Free VIP Korean Four Pillars PDF for honest feedback

Body:

```text
Hi Talie Tarot team,

I run Cheonglim Saem, a Korean Four Pillars reading service in English.

I am offering a free VIP PDF to a small number of astrology, tarot, K-culture, and self-reflection creators for honest feedback. The reading is framed as culture + self-reflection, not prediction, and it checks birthplace, timezone, DST, and true solar time for people born anywhere in the world.

No scripted praise. If it is useful, you can share your honest reaction; if not, private feedback is enough.

Review application:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Share kit and sample PDFs:
https://cheonglimsaju.com/promo-assets.html

Free mini preview, if you want to test the style first:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

If interested, the review page will format the request email with creator handle, platform, delivery email, and birth details for the sample PDF.

Thank you.
Cheonglim Saem
aideseobot@gmail.com
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,talie-tarot-001,sent to talietarot@gmail.com,free VIP review application URL included
```

## 6. hbbtarot

Source: https://linktr.ee/hbbtarot

Observed public contact evidence:

- The Linktree page says `Contact : hbbtarot@gmail.com`.
- Fit: tarot and astrology audience, existing paid consultation audience.

To:

hbbtarot@gmail.com

Subject:

Free VIP Korean Four Pillars PDF for honest feedback

Body:

```text
Hi hbbtarot,

I run Cheonglim Saem, a Korean Four Pillars reading service in English.

I am offering a free VIP PDF to a small number of astrology, tarot, K-culture, and self-reflection creators for honest feedback. The reading is framed as culture + self-reflection, not prediction, and it checks birthplace, timezone, DST, and true solar time for people born anywhere in the world.

No scripted praise. If it is useful, you can share your honest reaction; if not, private feedback is enough.

Review application:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Share kit and sample PDFs:
https://cheonglimsaju.com/promo-assets.html

Free mini preview, if you want to test the style first:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

If interested, the review page will format the request email with creator handle, platform, delivery email, and birth details for the sample PDF.

Thank you.
Cheonglim Saem
aideseobot@gmail.com
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,hbbtarot-001,sent to hbbtarot@gmail.com,free VIP review application URL included
```

## 7. BB Soto

Source: https://bbsoto.com/

Observed public contact evidence:

- The site offers tarot readings, astrology reports, and content marketing.
- The public contact block lists `message@bbsoto.com`.

To:

message@bbsoto.com

Subject:

Free Korean Four Pillars PDF for honest feedback

Body:

```text
Hi BB,

I run Cheonglim Saem, an English Korean Four Pillars / Saju project.

The offer sits near astrology/tarot audiences, but the framing is Korean culture + self-reflection, not prediction. It checks birthplace, timezone, DST, and true solar time before interpretation for people born anywhere in the world.

I am offering a free VIP PDF to a small number of astrology, tarot, and self-reflection creators for honest feedback. No scripted praise; private critique is fine.

Review application:
https://cheonglimsaju.com/free-vip-review.html?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch

Share kit and sample PDFs:
https://cheonglimsaju.com/promo-assets.html

Free mini preview:
https://cheonglimsaju.com/?utm_source=outreach&utm_medium=email&utm_campaign=kfortune_launch#free-preview

Thank you.
Cheonglim Saem
aideseobot@gmail.com
```

Evidence log after sending:

```csv
2026-05-16T__:__:__+09:00,outreach_sent,email,bb-soto-001,sent to message@bbsoto.com,free VIP review application URL included
```

## Deferred: DivineShineTarot

Recheck public contact before sending. Do not send from stale search snippets.

## Daily Send Rule

- Send only 3 personalized messages per day until replies begin.
- Do not send anything until the owner explicitly approves that exact outbound batch.
- Do not send repeated follow-ups sooner than 5 days.
- If a creator replies no, mark `declined` and do not contact again.
- If a creator applies, log `lead_type: free_vip_review_application` in `marketing/evidence-log.csv`.
- If a creator posts publicly, log the post URL and screenshot path.
