#!/usr/bin/env python3
import coloredlogs
import logging
import sys


logger = logging.getLogger(__name__)


def repeat(count: int = 3):
    def _repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return _repeat


@repeat(count=5)
def greet(who: str):
    logger.info(f"Hello {who}!")


def retryable(max_attempts=3):
    def _retryable(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == max_attempts:
                        raise e
                    logger.warning(f"Retry {i+1}: {func.__name__}...")

        return wrapper

    return _retryable


@retryable()
def raise_no_exception(status: str) -> str:
    logger.info(f"raise_no_exception({status}) is called and raises no exception.")
    return status


@retryable(max_attempts=4)
def always_raise_exception():
    logger.info("always_raise_exception() is called and raises an exception.")
    raise RuntimeError("Test exception.")


def main():
    logging.raiseExceptions = False
    coloredlogs.install(
        stream=sys.stdout,  # default: sys.stderr
        level="DEBUG",
        fmt="%(levelname)s %(message)s",
    )

    greet("alice")
    status = raise_no_exception("ok")
    logger.info(f"status: {status}")
    try:
        always_raise_exception()
    except Exception as e:
        logger.error("Unexpected error occurred.", exc_info=e)


if __name__ == "__main__":
    main()
