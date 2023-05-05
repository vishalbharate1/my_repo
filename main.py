from SMS.logger import logging
from SMS.exception import SMSException
import sys
import os
from SMS.utils import get_collection_as_dataframe

'''def test_logger_exception():
    try:
        logging.info("Starting the test_logger_exception")
        result=4/0
        print(result)
        logging.info("Ending the test_logger_exception")
    except Exception as e:
        logging.debug(str(e))
        raise SMSException(e,sys)'''

    
if __name__ == '__main__':
    try:
        #test_logger_exception()
        get_collection_as_dataframe(database_name='SMS_My_Repo',collection_name='SMS_Data')
    except Exception as e:
        print(e)