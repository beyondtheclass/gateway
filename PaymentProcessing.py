from PaymentProviders import *


class PaymentProcessing():

    def payment_process(self, body):
        amount = body["Amount"]
        if amount < 20:
            cheap_payment_gateway = CheapPaymentGateway()
            response = cheap_payment_gateway.process_payment(body)
            return response
    
        elif amount >= 20 and amount <= 500:
            if ExpensivePaymentGateway.is_available:    
                expensive_gateway = ExpensivePaymentGateway()
                response = expensive_gateway.process_payment(body)                
                return response

            else:                               # try once with cheap payment if expensive payment not available
                cheap_payment_gateway = CheapPaymentGateway()
                response = cheap_payment_gateway.process_payment(body)
                return response

        else:
            premium_gateway = PremiumPaymentGateway()
            for index in range(3):                 # Retry upto 3 times
                response = premium_gateway.process_payment(body)
                if response['status_code'] == 200:
                    break
            return response   