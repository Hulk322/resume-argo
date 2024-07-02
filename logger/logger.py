##@Logger Module
#This module is used to define a standard logging format.

# Import system libraries
import logging
import sys, os
from logging.handlers import TimedRotatingFileHandler

# Import manually defined modules
from logger import logger_config
from logger.linear_exceptions_formatting import LinearExceptionFormatter


##This class is used to define standard logging formats.
#It has three functions as below:-
#, get_console_handler()
#, get_file_handler()
#, get_logger()
class standardLogger(object):

    ## This function will set logging format for console output.
    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        log_format = LinearExceptionFormatter(
            logger_config.LOG_MESSAGE_FORMAT,
            logger_config.LOG_TIMINING_FORMAT)
        console_handler.setFormatter(log_format)
        return console_handler

    ## This function will set logging format for file output.
    # LOG_FILE is defined in logger_config.py
    def get_file_handler(self):
        if not os.path.exists(logger_config.DATASET_FOLDER):
            os.mkdir(logger_config.DATASET_FOLDER)
        file_handler = TimedRotatingFileHandler(
            logger_config.DATASET_FOLDER + logger_config.LOG_FILE,
            when='midnight')
        log_format = LinearExceptionFormatter(
            logger_config.LOG_MESSAGE_FORMAT,
            logger_config.LOG_TIMINING_FORMAT)
        file_handler.setFormatter(log_format)
        return file_handler

    ## This function will build a custom logger with provided name.
    #  @param self The object pointer.
    #  @param logger_name is name of the logger.
    #  @param kind_of_logger can be console, file or both just check the logger_config.py file for specific names.
    def get_logger(self,
                   logger_name,
                   kind_of_logger=logger_config.BOTH_CONSOLE_AND_FILE_LOGGER):
        logger = logging.getLogger(logger_name)
        logger.setLevel(
            logging.DEBUG)  # better to have too much log than not enough
        if kind_of_logger == logger_config.CONSOLE_LOGGER or kind_of_logger == logger_config.BOTH_CONSOLE_AND_FILE_LOGGER:
            logger.addHandler(self.get_console_handler())
        if kind_of_logger == logger_config.FILE_LOGGER or kind_of_logger == logger_config.BOTH_CONSOLE_AND_FILE_LOGGER:
            logger.addHandler(self.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger


if __name__ == '__main__':
    test_logger = standardLogger().get_logger("Testing Logs")
    test_logger.warning("This is a warning message")
