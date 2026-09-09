import pandas as pd

from src.transform.customer_transformer import CustomerTransformer


transformer = CustomerTransformer()


def test_city_title_case():

    df = pd.DataFrame(
        {
            "customer_city": ["sao paulo"],
            "customer_state": ["sp"]
        }
    )

    result = transformer.transform(df)

    assert result["customer_city"][0] == "Sao Paulo"


def test_state_uppercase():

    df = pd.DataFrame(
        {
            "customer_city": ["rio de janeiro"],
            "customer_state": ["rj"]
        }
    )

    result = transformer.transform(df)

    assert result["customer_state"][0] == "RJ"