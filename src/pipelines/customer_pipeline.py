from pathlib import Path
from src.extract.customer_extractor import CustomerExtractor
from src.validation.customer_validator import CustomerValidator
from src.transform.customer_transformer import CustomerTransformer
from src.load.postgres_loader import PostgreSQLLoader
from src.utils.logger import logger
from src.config.settings import DATABASE_URL


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "raw" / "olist_customers_dataset.csv"


def run_customer_pipeline():

    logger.info("========== CUSTOMER PIPELINE START ==========")

    extractor = CustomerExtractor(DATA_PATH)
    validator = CustomerValidator()
    transformer = CustomerTransformer()

    loader = PostgreSQLLoader(DATABASE_URL)

    # Extract
    df = extractor.get_dataframe()

    # Validate
    df = validator.validate(df)

    # Transform
    df = transformer.transform(df)

    # Load
    loader.load(
    df=df,
    table_name="customers")

    logger.info("========== CUSTOMER PIPELINE END ==========")