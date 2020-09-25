from flask import abort
import datetime

class CustomValidation():
    
    def validate_credit_card_number(self, credit_card_number):

        if not credit_card_number:
            abort(400, "Credit Card Number can not be empty")

        credit_card_number = str(credit_card_number)

        if len(credit_card_number) != 16 or not credit_card_number.isnumeric():
            abort(400, "Credit Card Number value is not correct")


    def validate_card_holder(self, card_holder):
        if not card_holder:
            abort(400, "Card Holder can not be empty")

        card_holder = str(card_holder)
        card_holder1 = card_holder.replace(' ', '')

        if not card_holder1.isalpha():
            abort(400, "Card Holder Name is not valid")


    def validate_expiration_date(self, expiration_date):
        if not expiration_date:
            abort(400, "Expiration date can not be empty")

        expiration_date_new_format = ""
        if expiration_date:
            expiration_date_new_format = datetime.datetime.strptime(expiration_date, "%d-%m-%Y %H:%M:%S")
            expiration_date_new_format = expiration_date_new_format.strftime("%Y%m%d %H:%M:%S")
            expiration_date_new_format = datetime.datetime.strptime(expiration_date_new_format, "%Y%m%d %H:%M:%S")
        
        print(expiration_date, expiration_date_new_format, datetime.datetime.now())
        if expiration_date_new_format and expiration_date_new_format < datetime.datetime.now():
            abort(400, "Credit Card Expiry can not be in past")


    def validate_security_code(self, security_code):
        if not security_code:
            return 

        if type(security_code) != str or len(security_code) != 3:
            abort(400, "Credit Card Security code is invalid")


    def validate_amount(self, amount):
        if not amount:
            abort(400, "Amount can not be empty")

        if type(amount) == str:
            abort(400, "Amount can be in alpha numeric")

        if amount <= 0:
            abort(400, "Amount can not be less than equal to 0")


