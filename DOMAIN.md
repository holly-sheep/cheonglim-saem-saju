# Custom Domain Target

Target public brand domain: `cheonglimsaem.com`

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
CNAME www cheonglimsaem.com
```

After DNS is active:

1. Rename `CNAME.example` to `CNAME`.
2. Update canonical URLs, Open Graph URLs, `robots.txt`, and `sitemap.xml` from `https://hollysheep-ai.github.io/cheonglim-saem-saju/` to `https://cheonglimsaem.com/`.
3. Push to `main`.
4. Confirm `gh api repos/hollysheep-ai/cheonglim-saem-saju/pages` reports `"cname":"cheonglimsaem.com"`.
