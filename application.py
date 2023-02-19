import os
from dotenv import load_dotenv

from utils.accessEnv import accessEnv
from utils.logger import Logger

# loading environment variables
load_dotenv()

logger = Logger(name=__name__, env='production').getLogger()
