import pandas as pd
from sqlalchemy import create_engine
from src.load.base_loader import BaseLoader
from src.utils.logger import logger
from src.config.settings import POSTGRES_SCHEMA
from src.utils.db_utils import insert_on_conflict_nothing


class PostgreSQLLoader(BaseLoader):

    def __init__(self, connection_string):

        self.connection_string = connection_string

    def load(
        self,
        df: pd.DataFrame,
        table_name: str,
        method=insert_on_conflict_nothing,
        schema=POSTGRES_SCHEMA
    ):

        logger.info("Connecting PostgreSQL...")

        engine = create_engine(self.connection_string)

        logger.info("Loading dataframe...")

        df.to_sql(
            name=table_name,
            schema=schema,
            con=engine,
            if_exists="append",
            index=False,
            method=method
        )

        logger.info(f"Loaded {len(df)} rows.")

        logger.info(f"Loading '{table_name}' into schema '{schema}'...")