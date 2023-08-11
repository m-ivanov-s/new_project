import logging

logging.basicConfig(filename="my_log.log", filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def get_logger():
    return logger
