#!/usr/bin/env python

import logging
import sys
from payment_gateway import PaymentGateway

def main():
    try:
        # Initialize Payment Gateway
        payment_gateway = PaymentGateway()

        # Add payment methods
        payment_gateway.add_payment_methods(['credit/debit cards', 'PayPal', 'Stripe'])

        # Redirect user to secure payment page
        payment_gateway.redirect_to_payment_page()

        # Accept payment details
        payment_gateway.accept_payment_details()

        # Process payment transactions
        payment_gateway.process_payment_transactions()

        # Display appropriate messages
        payment_gateway.display_messages()

    except Exception as e:
        # Log error for debugging
        logging.error(e)
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()