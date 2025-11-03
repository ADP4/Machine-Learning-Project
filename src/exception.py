import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed traceback information when an exception occurs.

    Parameters:
        error: The actual error/exception object.
        error_detail: The sys module (used to access exc_info for traceback).

    Returns:
        A formatted string with:
        - File name where the error occurred
        - Line number of the error
        - The error message itself
    """

    # exc_info() returns (exception_type, exception_value, traceback_object)
    _, _, exc_tb = error_detail.exc_info()

    '''Key parts inside the traceback object:

exc_tb.tb_frame → the current stack frame where the error occurred

exc_tb.tb_frame.f_code → the code object for that frame

exc_tb.tb_frame.f_code.co_filename → the filename of that code

exc_tb.tb_lineno → the line number within that file'''

    # Get file name from traceback -> frame -> code object
    file_name = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno 

    # Format a clean and informative error message
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] error message [{2}]"
    ).format(file_name, lineno, str(error))

    return error_message


class CustomException(Exception):
    """
    Custom exception class that extends Python's built-in Exception class.
    Adds clearer and more descriptive error messages using traceback details.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Constructor for CustomException.

        Parameters:
            error_message: The original error message.
            error_detail: The sys module for traceback extraction.
        """

        # Initialize base Exception with original message
        super().__init__(error_message)

        # Store the detailed traceback-enhanced message
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    def __str__(self):
        """
        Returns the string representation of the exception.
        When the exception is printed, the detailed message appears.
        """
        return self.error_message
    
#exception test

#if __name__ == "__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("anuja experimented with divide by zero")
#        raise CustomException(e,sys)