import pandas as pd
import pytest

from src.data_loader import load_price_data


def test_load_price_data():
    df = load_price_data("data/sample_prices.csv")
    assert "close" in df.columns
    assert len(df) > 0


def test_load_price_data_missing_columns(tmp_path):
    bad_file = tmp_path / "bad.csv"
    pd.DataFrame(
        {
            "date": ["2024-01-01"],
            "open": [100],
            "close": [101],
        }
    ).to_csv(bad_file, index=False)

    with pytest.raises(ValueError):
        load_price_data(str(bad_file))
