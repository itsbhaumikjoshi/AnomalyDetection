import os
import logging
from logging.handlers import TimedRotatingFileHandler

DEFAULT_LOGGING_FOLDER = os.path.join(os.getcwd(), 'logs')
DEFAULT_LOGGING_PATH = os.path.join(DEFAULT_LOGGING_FOLDER, 'prod')

def setupLogger(
    name,
    env="development",
    level=None,
    format="%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(lineno)d - %(message)s",
    filename=DEFAULT_LOGGING_PATH
):

    level = level or (logging.INFO if env == "production" else logging.DEBUG)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if env == "production":

        if not os.path.isdir(DEFAULT_LOGGING_FOLDER):
            os.makedirs(DEFAULT_LOGGING_FOLDER)

        formatter = logging.Formatter(format)

        handler = TimedRotatingFileHandler(DEFAULT_LOGGING_PATH, when="midnight")
        handler.suffix = "%d-%m-%Y.log"
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    
    return logger
