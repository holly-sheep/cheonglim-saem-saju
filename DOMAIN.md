# Custom Domain Target

Target public brand domain: `cheonglimsaju.com`

Do not commit this as `CNAME` until DNS resolves to GitHub Pages. If `CNAME` is deployed before the domain is purchased and pointed at GitHub Pages, the current working GitHub Pages funnel can redirect to a dead domain.

Required DNS records for the apex domain:

```text
A 185.199.108.153
A 185.199.109.153
A 185.199.110.153
A 185.199.111.153
```

Optional `www` record:

```text
CNAME www cheonglimsaju.com
```

After DNS is active:

1. Rename `CNAME.example` to `CNAME`.
2. Update canonical URLs, Open Graph URLs, `robots.txt`, and `sitemap.xml` to `https://cheonglimsaju.com/`.
3. Push to `main`.
4. Confirm `gh api repos/holly-sheep/cheonglim-saem-saju/pages` reports `"cname":"cheonglimsaju.com"`.
