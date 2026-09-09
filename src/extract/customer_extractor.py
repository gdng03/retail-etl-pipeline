import pandas as pd 
from src.extract.base_extractor import BaseExtractor
from src.utils.logger import logger

class CustomerExtractor(BaseExtractor):

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def get_dataframe(self):
        logger.info("Start extracting dataset...")

        self.check_file_exists()
        logger.info("File found.")

        logger.info("Reading CSV...")
        df = self.read_csv()
        logger.info(f"Loaded {len(df)} records.")

        return df