import logging
from pathlib import Path 
import sys

BASE_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"

# create Formatter
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# create file handle
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# create stream handle
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# create logger
logger = logging.getLogger("retail_etl_pipeline")
logger.setLevel(logging.INFO)
logger.propagate = False # avoid propagating the report back up to the root logger

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

