import os
import sys

class SMSException(Exception):
    def __init__(self, error_message: Exception, error_details : sys):
        super().__init__(error_message)
        self.error_message=SMSException.error_message_details(error_message,error_details=error_details)
    
    @staticmethod
    def error_message_details(error:Exception, error_details: sys):
        _, _, exc_tb=error_details.exc_info()
        line_number= exc_tb.tb_frame.f_lineno

        file_name= exc_tb.tb_frame.f_code.co_filename

        error_message= f"Error occured python script name [ { file_name } ]" 
        f"line number [ { exc_tb.tb_lineno}] error message [{ error }]"

        return error_message

def __str__(self):
       return self.error_message

def __repr__(self):
     return SMSException.__name__.__str__()

