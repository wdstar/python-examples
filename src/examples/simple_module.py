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


class SimpleClass:
    def __init__(self):
        self.logger = logging.getLogger(__name__ + "." + self.__class__.__name__)
        self.logger.addHandler(logging.NullHandler())
        self.logger.info("creating an instance of SimpleClass")

    def class_logging(self):
        self.logger.debug("debug message")
        self.logger.info("info message")
        self.logger.warn("warn message")
        self.logger.error("error message")
        self.logger.critical("critical message")
