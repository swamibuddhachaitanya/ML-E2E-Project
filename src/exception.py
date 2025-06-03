import sys
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    """
    This function returns the error message with details.
    """
    _,_,exc_tb= error_detail.exc_info()
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom Exception class to handle exceptions in the project.
    """
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    try:
        a = 1
        b = 0
        div = a/b
    except Exception as e:
        logging.error("Divide by zero error occurred")
        raise CustomException(e, sys)