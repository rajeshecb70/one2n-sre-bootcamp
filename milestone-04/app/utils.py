import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    handler = RotatingFileHandler('logs/api.log', maxBytes=1024 * 1024, backupCount=10)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[handler, logging.StreamHandler()])
