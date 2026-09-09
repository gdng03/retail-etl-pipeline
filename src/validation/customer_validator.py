from src.validation.base_validator import BaseValidator
from src.utils.logger import logger
import pandas as pd

class CustomerValidator(BaseValidator):


    REQUIRED_COLUMNS = [

        "customer_id",

        "customer_unique_id",

        "customer_zip_code_prefix",

        "customer_city",

        "customer_state"

    ]

    def validate(self, df: pd.DataFrame) -> pd.DataFrame:   

        logger.info("Checking validate...")

        self.validate_not_empty(df)
        logger.info("Not empty.")

        self.column_validate(df, self.REQUIRED_COLUMNS)
        logger.info("Not missing column.")

        logger.info("Customer dataset validation completed.")
        
        return df