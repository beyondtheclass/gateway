# works with both python 2 and 3
from __future__ import print_function

import africastalking

class CARD:
    def __init__(self):
		# Set your app credentials
        self.username = "YOUR_USERNAME"
        self.api_key = "YOUR_API_KEY"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the payments service
        self.payment = africastalking.Payment

    def checkout(self):
        # Set the name of your Africa's Talking payment product
        productName = "ABC"

        # Set the details of the payment card to be charged
        card = {
            'number': '3234324235452345',
            'countryCode': 'NG',
            'cvvNumber': 3343,
            'expiryMonth': 3,
            'expiryYear': 2022,
            'authToken': '3322'
        }

        # If you already have a valid checkout token for the card user, as a result of a previous successful validation,
        # you can charge the card by passing in the checkout token instead of sending the full card information again.
		checkout_token=None

        # Set The 3-Letter ISO currency code and the checkout amount
        currencyCode = "NGN"
        amount = 100.50

        # Set a description of the transaction to be displayed on the clients statement
        narration='Small Chops Checkout'

        # Set any metadata that you would like to send along with this request.
        # This metadata will be included when we send back the final payment notification
		metadata     = {
  			'requestId' : "1234",
  			'applicationId' : "abcde"
		}

        # That's it, hit send and we'll take care of the rest
        try:
            res = self.payment.card_checkout(productName, currencyCode, amount, narration, card, checkout_token, metadata)

            # Now you must validate the checkout by sending the transactionId generated from this
    		# request and an OTP you collected from the user. See Card Checkout Validate.
            print (res)
        except Exception as e:
            print ("Received error response:%s" %str(e))


    def validate(self):
        # Set the transactionId you got from the card checkout charge request
        transaction_id = "ATPid_7444b64859882d23c9ee9621276fc7c7f"

        # Set the OTP given to you by the user you're charging
        otp = "1342"

        # That's it, hit send and we'll take care of the rest
        try:
            res = self.payment.validate_card_checkout(transaction_id, otp)
            print (res)
        except Exception as e:
            print ("Received error response:%s" %str(e))

if __name__ == '__main__':
