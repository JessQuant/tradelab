import pandas as pd

from src.features import add_features


def test_add_features_creates_expected_columns():
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2024-01-01",
                    "2024-01-02",
                    "2024-01-03",
                    "2024-01-04",
                    "2024-01-05",
                    "2024-01-08",
                    "2024-01-09",
                    "2024-01-10",
                    "2024-01-11",
                    "2024-01-12",
                    "2024-01-15",
                    "2024-01-16",
                    "2024-01-17",
                    "2024-01-18",
                    "2024-01-19",
                    "2024-01-22",
                    "2024-01-23",
                    "2024-01-24",
                    "2024-01-25",
                    "2024-01-26",
                ]
            ),
            "open": list(range(100, 120)),
            "high": list(range(101, 121)),
            "low": list(range(99, 119)),
            "close": list(range(100, 120)),
            "volume": [1000 + 10 * i for i in range(20)],
        }
    )

    result = add_features(df)

    assert "daily_return" in result.columns
    assert "cumulative_return" in result.columns
    assert "ma_short" in result.columns
    assert "ma_long" in result.columns
    assert "momentum" in result.columns
    assert "rolling_volatility" in result.columns
