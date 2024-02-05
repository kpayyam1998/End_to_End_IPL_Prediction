import sys

class customexception(Exception):
    def __init__(self,error_message,errordetail:sys ):
        self.error_message=error_message
        _,_,exc_tb=errordetail.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return "Error Occured in the python scirpt[{0}] and line number[{1}] error message[{2}]".format(self.filename,self.lineno,str(self.error_message))
