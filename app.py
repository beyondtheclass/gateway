from flask import Flask, request,render_template
from Validation import CustomValidation
from PaymentProviders import *
from PaymentProcessing import *
import requests
from models import *                                                                        



# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_restful import Resource, Api

app = Flask(__name__)

# api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/payments.db'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/price')
def price():
    return render_template('pricing.html')




@app.route('/tests/', methods=['POST', 'GET'])
def my_test_endpoint():

    try:

        user_1 =  {

        "CreditCardNumber":"1234567490123456",
        "CardHolder" : "XYZ",
        "ExpirationDate" : "25-10-2022 16:24:25",
        "SecurityCode":"345",
        "Amount" : 550

        }

        res = requests.post('http://127.0.0.1:5000/processpayment', json=user_1)

        return res.json()

    except Exception as e:
        return json.dumps({}), 400, {'ContentType':'application/json'} 




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
