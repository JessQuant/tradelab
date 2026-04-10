import pandas as pd

REQUIRED_COLUMNS = ["date", "open", "high", "low", "close", "volume"]


def load_price_data(filepath):
    """
    Load historical price data from a CSV file and return a cleaned DataFrame.
    """
    df = pd.read_csv(filepath)

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    return df
