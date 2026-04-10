def clean_price_data(df):
    """
    Remove duplicate rows, drop missing values in required columns,
    and reset the index.
    """
    required_columns = ["date", "open", "high", "low", "close", "volume"]

    df = df.drop_duplicates(subset=["date"])
    df = df.dropna(subset=required_columns)
    df = df.reset_index(drop=True)

    return df
