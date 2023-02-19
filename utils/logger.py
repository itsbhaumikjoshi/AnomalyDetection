import os
import time
import logging
from logging.handlers import TimedRotatingFileHandler

DEFAULT_LOGGING_FOLDER = os.path.join(os.getcwd(), 'logs')
DEFAULT_LOGGING_PATH = os.path.join(DEFAULT_LOGGING_FOLDER, 'prod')

class Logger():
    
    def __init__(
        self,
        name,
        env="development",
        level=None,
        format="%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(lineno)d - %(message)s",
        filename=DEFAULT_LOGGING_PATH
    ):
        level = level or (logging.INFO if env == "production" else logging.DEBUG)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if env == "production":

            if not os.path.isdir(DEFAULT_LOGGING_FOLDER):
                os.makedirs(DEFAULT_LOGGING_FOLDER)

            formatter = logging.Formatter(format)

            handler = TimedRotatingFileHandler(DEFAULT_LOGGING_PATH, when="S", interval=30)
            handler.suffix = "%d-%m-%Y.log"
            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

    def getLogger(self):
        return self.logger
