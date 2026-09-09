from src.transform.base_transformer import BaseTransformer
from src.utils.logger import logger
import pandas as pd

class CustomerTransformer(BaseTransformer):

    def transform(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Start transforming customer dataset...")

        # remove space
        logger.info("Removing leading/trailing spaces from text columns...")

        text_columns = ["customer_city", "customer_state"]
        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()

        # standardize 
        logger.info("Standardizing city names...")

        df["customer_city"] = df["customer_city"].str.title()

        logger.info("Standardizing state codes...")

        df["customer_state"] = df["customer_state"].str.upper()

        # remove duplicate
        logger.info("Removing duplicate customers...")

        before = len(df)
        df = df.drop_duplicates()
        after = len(df)

        logger.info(f"Removed {after - before} duplicate rows.")

        # check missing
        logger.info("Checking missing values...")

        missing = df.isnull().sum().sum()

        logger.info(f"Total missing values: {missing}")

        # reset index
        df = df.reset_index(drop = True)

        logger.info("Transformatiom completed.")
        return df