def add_features(df, short_window=3, long_window=5, momentum_window=3):
    """
    Add simple quantitative features to the price data.
    """
    df = df.copy()

    df["daily_return"] = df["close"].pct_change()
    df["cumulative_return"] = (1 + df["daily_return"]).cumprod() - 1
    df["ma_short"] = df["close"].rolling(window=short_window).mean()
    df["ma_long"] = df["close"].rolling(window=long_window).mean()
    df["momentum"] = df["close"] - df["close"].shift(momentum_window)

    return df
