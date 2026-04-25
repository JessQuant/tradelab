import pandas as pd

from src.features import add_features


def test_add_features_creates_columns():
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2024-01-01",
                    "2024-01-02",
                    "2024-01-03",
                    "2024-01-04",
                    "2024-01-05",
                ]
            ),
            "open": [100, 101, 102, 103, 104],
            "high": [101, 102, 103, 104, 105],
            "low": [99, 100, 101, 102, 103],
            "close": [100, 101, 102, 103, 104],
            "volume": [1000, 1100, 1200, 1300, 1400],
        }
    )

    result = add_features(df)

    assert "daily_return" in result.columns
    assert "cumulative_return" in result.columns
    assert "ma_short" in result.columns
    assert "ma_long" in result.columns
    assert "momentum" in result.columns
