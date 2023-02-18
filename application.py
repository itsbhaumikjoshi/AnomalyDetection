import os
from dotenv import load_dotenv

from utils.accessEnv import accessEnv
from utils.setupLogger import setupLogger

# loading environment variables
load_dotenv()

logger = setupLogger(__name__, env=accessEnv("ENV"))
