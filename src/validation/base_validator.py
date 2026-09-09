from abc import ABC, abstractmethod
import pandas as pd

class BaseValidator(ABC):

    def validate_not_empty(self, df: pd.DataFrame):
        if df.empty:
            raise ValueError("DataFrame is empty.")

    def column_validate(self, df:pd.DataFrame, required_column: list):
        missing_columns = [col for col in required_column if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns: {missing_columns}")

    @abstractmethod
    def validate(self, df: pd.DataFrame):

        pass

