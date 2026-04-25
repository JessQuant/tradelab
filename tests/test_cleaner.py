import pandas as pd

from src.cleaner import clean_price_data


def test_clean_price_data_removes_duplicates_and_missing():
    df = pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-01", "2024-01-02"],
            "open": [100, 100, None],
            "high": [101, 101, 102],
            "low": [99, 99, 100],
            "close": [100, 100, 101],
            "volume": [1000, 1000, 1100],
        }
    )

    cleaned = clean_price_data(df)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["date"] == "2024-01-01"
