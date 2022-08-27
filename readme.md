# Install Python3 using this link `https://www.python.org/downloads/`

# Install virtualenvironment in your machine using command below
# python3 -m pip install --user virtualenv

# Create Virtualenvironment in the root folder
# python3 -m venv venv

# Activate the Virtual Environment
# source venv/bin/activate

# Run below commands to run this on your local system

# export FLASK_APP=app.py
# export FLASK_ENV=development
# export FLASK_DEBUG=0


# /home/daffolap-834/Downloads/flask_demo/venv/bin/python -m flask run  (The path will change according to your directory in which you clone this project)


Sample API Request body :
 {
    "CreditCardNumber":"1234567490123456",
    "CardHolder" : "XYZ",
    "ExpirationDate" : "25-10-2020 16:24:25",
    "SecurityCode":"345",
    "Amount" : 550
 }

Sample API Endpoint : 
    http://127.0.0.1:5000/processpayment
Method:
    post

Sample Response:
 # In case of success
{
    "Amount": 550,
    "message": "Success, Your Transaction has been successful",
    "status_code": 200
}

# In case of failure
{
    "Amount": 550,
    "message": "Sorry, Your Transaction has been Failed",
    "status_code": 500
}

