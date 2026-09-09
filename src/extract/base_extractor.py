from pathlib import Path
from abc import ABC, abstractmethod
import pandas as pd


class BaseExtractor(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def check_file_exists(self):
        if not Path(self.file_path).exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}")

    def read_csv(self):
        return pd.read_csv(self.file_path)

    @abstractmethod
    def get_dataframe(self):
        pass
