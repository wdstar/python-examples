# coding: utf-8
import logging

# module logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def module_logging():
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    logger.critical("critical message")
