

class PremiumPaymentGateway():
    is_available = True
    def process_payment(self, body):
        '''
            Process Payment using the Premium Gateway.
            Transaction business logic in ATOMIC way.
            Return status code will be 200, 500  
        '''
        response = {}
        response["Amount"] = body["Amount"]
        if True:
            response["status_code"] = 200
            response["message"] = "Success, Your Transaction has been successful"
        else:
            response["status_code"] = 500
            response["message"] = "Sorry, Your Transaction has been Failed"  

        return response

class ExpensivePaymentGateway():
    is_available = False
    def process_payment(self, body):
        '''
            Process Payment using the Expensive Gateway.
            Transaction business logic in ATOMIC way.
            Return status code will be 200, 500  
        '''
        response = {}
        response["Amount"] = body["Amount"]
        if False:
            response["status_code"] = 200
            response["message"] = "Success, Your Transaction has been successful"
        else:
            response["status_code"] = 500
            response["message"] = "Sorry, Your Transaction has been Failed"  
        return response
        


class CheapPaymentGateway():
    is_available = True
    
    def process_payment(self, body):
        '''
            Process Payment using the Cheap Gateway.
            Transaction business logic in ATOMIC way.
            Return status code will be 200, 500  
        '''
        response = {}
        response["Amount"] = body["Amount"]

        if True:
            response["status_code"] = 200
            response["message"] = "Success, Your Transaction has been successful"
        else:
            response["status_code"] = 500
            response["message"] = "Sorry, Your Transaction has been Failed"   

        return response
        

