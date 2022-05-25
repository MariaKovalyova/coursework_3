"""Логгирование"""

import logging

def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("logs/basic.txt")
    logger.addHandler(file_handler)

    formater = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formater)

    return logger

