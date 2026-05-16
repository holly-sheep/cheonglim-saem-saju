#!/usr/bin/env bash
set -euo pipefail

site_out="${1:-_site}"

case "$site_out" in
  ""|"/"|".")
    echo "Refusing unsafe output directory: ${site_out:-<empty>}" >&2
    exit 1
    ;;
esac

rm -rf -- "$site_out"
mkdir -p "$site_out"

cp ./*.html "$site_out"/
cp robots.txt sitemap.xml "$site_out"/
cp ./*.xml "$site_out"/
cp ./*.txt "$site_out"/
cp -R assets "$site_out"/assets

if [[ -f CNAME ]]; then
  cp CNAME "$site_out"/CNAME
fi
