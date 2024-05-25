import africastalking
from typing import List
import decimal


class Services:
    def __init__(self):
        username = "notifygrace"    # use 'sandbox' for development in the test environment
        api_key = "5f421340bb21767c7c9a42ea1cf544f643d9c2639517d6c2bc96ab638c30a012"      # use your sandbox app API key for development in the test environment
        self.handler = africastalking
        self.handler.initialize(username, api_key)

    def debug(self,message):
        sms = self.handler.SMS
        sms.send(message, ["+256786842944"])


    def send_message(self,numbers:List[str], message):
        if message:
            # message = "\U0001F6A8 Bio-gas System Monitor \U0001F6A8 \n" + message
            sms = self.handler.SMS
            response = sms.send(message, numbers)
            return response
        return "Every thing is okay"