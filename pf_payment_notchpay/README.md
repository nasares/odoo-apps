# Notchpay Odoo module

Mobile Money payment integration with the Notchpay provider in Odoo (Cameroon Orange Money and MTN Mobile Money payments)

## Supported features

- Notchpay as provider for Mobile Money Payment
- Available only for Currency XAF with Orange Money and MTN Mobile Money in Cameroon
- Work with website_sale only (e-commerce)
- Intialize payment
- Process Payment
- Retrieve payment and set Odoo payment transaction status based on Notchpay API response

## Not implemented 

- Webhook integration
- Usage in other odoo modules
- Mobile money journal (accounting)
- Refunds
- Tokenization
- Automatic payment method link with Notchpay provider
- No icon, no unit test, no demo data, no translation (only english is supported)
- No secret key, only public key is supported yet

## Usage

- Install `l10n_syscohada`, and `website_sale`
- Install `pf_payment_notchpay`
- Go to Invoicing or Accounting -> Configuration -> Online Payments -> Payment Providers
- Activate Notchpay
- Paste your Notchpay public key
- Enable payment methods in the Configuration tab
- Set also currency, country and payment journal
- Go the the website, and buy a product

## Technical details

- Create a Notchpay account : https://notchpay.co
- API reference : https://developer.notchpay.co/api-reference 
- Initialize a payment : https://developer.notchpay.co/api-reference/initialize-a-payment 
- Retrieve a payment : https://developer.notchpay.co/api-reference/retrieve-a-payment
- Mobile money : https://developer.notchpay.co/accept-payments/mobile-money
- Phone numbers for testing:
    - +237670000000 (success)
    - +237670000001 (insufficient funds)
    - +237670000002 (failure)
    - +237670000003 (timeout)
    - +237670000004 (canceled)

Inspired from the [payment_flutterwave](https://github.com/odoo/odoo/tree/18.0/addons/payment_flutterwave) module
