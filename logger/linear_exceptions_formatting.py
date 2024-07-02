##@Linear Exception Formatter is used to log exception and multilinear objects in a single line.
#This module is used to Classify Industry for a Job Title.

# SYSTEM IMPORT CLASS
import re
import logging
import traceback


##This class is used to convert multilinear output into single line output.
#It has two functions as below:-
#, formatException()
#, format()
class LinearExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        tb = re.sub("\n", "\t", traceback.format_exc(exc_info[2]))
        result = tb
        return result  # or format into one line however you want to

    def format(self, record):
        s = super(LinearExceptionFormatter, self).format(record)
        s = s.replace('\n', '\t')
        return s
