# coding: utf-8
import logging
import logging.config

logging.raiseExceptions = False  # for prod
# Programmatic root configuration.
logging.basicConfig(filename='sample.log', level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')
# File base configuration.
#logging.config.fileConfig('logging.conf')

# Logger specific programmatic configuration.
"""
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
"""

logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
