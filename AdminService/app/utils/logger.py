import logging
import sys

# Get logger
logger = logging.getLogger(__name__)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')

# set formatters
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add handlers to logger
logger.handlers = [stream_handler, file_handler]
# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)

# set log level
logger.setLevel(logging.INFO)