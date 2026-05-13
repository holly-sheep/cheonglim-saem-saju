# Public Landing Page

This folder is a static website. Upload the folder contents to any static host.

Configured payment links:

- Basic: https://www.paypal.com/ncp/payment/4MAPBL2JSJGVU
- Premium: https://www.paypal.com/ncp/payment/3CF8HLMDFEG86
- VIP: https://www.paypal.com/ncp/payment/4BY7WQZQV55SC

Daily revenue target paths:

- 2 Basic orders = KRW 19,800 before platform fees
- 1 Premium order = KRW 19,900 before platform fees
- 1 VIP order = KRW 39,900 before platform fees

The intake page sends email to `aideseobot@gmail.com`.
Fulfillment is designed to be handled by the `saju/mail_order_worker.py` automation in the local Saju project: the worker polls the inbox every few hours, matches intake emails against PayPal payment notifications, generates a PDF, and replies by email.

No server is required.
