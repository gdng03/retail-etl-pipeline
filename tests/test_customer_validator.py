import pandas as pd
import pytest

from src.validation.customer_validator import CustomerValidator


validator = CustomerValidator()


def test_validate_success():

    df = pd.DataFrame(
        {
            "customer_id": ["1"],
            "customer_unique_id": ["A"],
            "customer_zip_code_prefix": [12345],
            "customer_city": ["sao paulo"],
            "customer_state": ["sp"]
        }
    )

    result = validator.validate(df)

    assert result.equals(df)


def test_validate_empty_dataframe():

    df = pd.DataFrame()

    with pytest.raises(ValueError):

        validator.validate(df)