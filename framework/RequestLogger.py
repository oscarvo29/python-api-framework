import logging

log_file = 'app.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
        ]
)

logger = logging.getLogger("server")
