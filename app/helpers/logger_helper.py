import logging
import os
import sys


def init_logger():
    logger = logging.getLogger("flask-bp-app")
    logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def get_logger():
    return logging.getLogger("xm-app")
