#!/usr/bin/env python3
import logging
import logging.config
import time
import simple_module
import packagea.module_a

logging.raiseExceptions = False  # for prod
# logging.Formatter.converter = time.localtime
logging.Formatter.converter = time.gmtime
# Programmatic root configuration.
logging.basicConfig(
    # filename="sample.log",
    handlers=[logging.StreamHandler(), logging.FileHandler("sample.log")],
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %Z %z",
)
# File base configuration.
# logging.config.fileConfig('logging.conf')

# Logger specific programmatic configuration.
"""
logger = logging.getLogger('simple_module')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.propagate = False
"""

logger = logging.getLogger(__name__)
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

simple_module.module_logging()
packagea.module_a.module_logging()

simple_class = simple_module.SimpleClass()
simple_class.class_logging()
