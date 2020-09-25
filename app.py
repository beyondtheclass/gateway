from flask import Flask, request
from Validation import CustomValidation
from PaymentProviders import *
from PaymentProcessing import *

# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)


@app.route('/processpayment', methods=["POST"])
def ProcessPayment():
    body = request.get_json(force=True)
    
    credit_card_number = body.get('CreditCardNumber', None)
    card_holder = body.get('CardHolder', None)
    expiration_date = body.get('ExpirationDate', None)
    security_code = body.get('SecurityCode', None)
    amount = body.get('Amount', None)
    
    validation_obj = CustomValidation()
    
    validation_obj.validate_credit_card_number(credit_card_number)
    validation_obj.validate_card_holder(card_holder)
    validation_obj.validate_expiration_date(expiration_date)
    validation_obj.validate_security_code(security_code)
    validation_obj.validate_amount(amount)

    payment_obj = PaymentProcessing()
    response = payment_obj.payment_process(body)
    return response

if __name__ == '__main__':
    app.run(debug=True)
