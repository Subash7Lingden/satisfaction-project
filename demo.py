from satisfaction.exception import CustomException
import sys
from satisfaction.logger import logging


try:
    a = 1/ "10"
except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)