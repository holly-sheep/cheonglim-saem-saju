# Public Landing Page

This folder is a static website. Upload the folder contents to any static host.

Public display prices:

- Basic: $9
- Premium: $19
- VIP: $39

Primary payment:

- Asset/network: USDT-TRC20 on TRON
- Address: `TPinvSovyuBHTVK1Kd6bUYYESMoSBxjgjJ`
- QR asset: `assets/usdt-tron-qr.png` (address-only QR)
- Amounts: current USDT equivalent of the USD package price, using the live USDT/USD estimate shown on the site.

The intake page sends email to `aideseobot@gmail.com`.
Fulfillment is designed to be handled by the `saju/mail_order_worker.py` automation in the local Saju project: the worker polls the inbox every few hours, matches intake emails against confirmed USDT deposit notifications or configured crypto checkout webhooks, generates a PDF, and replies by email.

No server is required for the static website. Automated fulfillment still depends on the local mail worker and any configured payment webhook receiver.
