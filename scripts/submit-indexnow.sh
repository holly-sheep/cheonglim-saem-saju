#!/usr/bin/env bash
set -euo pipefail

HOST="cheonglimsaju.com"
KEY="cheonglim-saju-indexnow-20260516-7ab7"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
ENDPOINT="${INDEXNOW_ENDPOINT:-https://api.indexnow.org/indexnow}"

payload=$(cat <<JSON
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": [
    "https://${HOST}/",
    "https://${HOST}/bio.html",
    "https://${HOST}/start.html",
    "https://${HOST}/free-korean-saju-reading.html",
    "https://${HOST}/overseas-birth-saju.html",
    "https://${HOST}/saju-in-english.html",
    "https://${HOST}/korean-saju-reading-online.html",
    "https://${HOST}/true-solar-time-saju.html",
    "https://${HOST}/saju-without-birth-time.html",
    "https://${HOST}/korean-birthday-reading.html",
    "https://${HOST}/korean-compatibility-reading.html",
    "https://${HOST}/kfortune-2026-2027-timing.html",
    "https://${HOST}/basic-korean-saju-report.html",
    "https://${HOST}/free-vip-review.html",
    "https://${HOST}/promo-assets.html"
  ]
}
JSON
)

curl -sS -i \
  -H "Content-Type: application/json; charset=utf-8" \
  --data "${payload}" \
  "${ENDPOINT}"
