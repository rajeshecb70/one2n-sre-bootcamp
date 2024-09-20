import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging():
    # Create a logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Set up a rotating log file handler (max size: 1MB, keep last 10 log files)
    file_handler = RotatingFileHandler('logs/api.log', maxBytes=1024 * 1024, backupCount=10)
    file_handler.setLevel(logging.INFO)

    # Define the format of log entries
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    file_handler.setFormatter(formatter)

    # Add the handler to the root logger
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(file_handler)

    # Optionally, log errors to stderr as well
    logging.getLogger().addHandler(logging.StreamHandler())
