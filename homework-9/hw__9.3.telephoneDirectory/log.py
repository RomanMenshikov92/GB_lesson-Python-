import logging
import os

path = 'homework-9/hw__9.3.telephoneDirectory'

logging.basicConfig(
    filename=os.path.join(path, 'db_telDir.log'),
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)
