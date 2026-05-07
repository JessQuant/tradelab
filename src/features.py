import pandas as pd


def add_features(
    df: pd.DataFrame,
    short_window: int = 5,
    long_window: int = 20,
    momentum_window: int = 5,
    volatility_window: int = 10,
) -> pd.DataFrame:
    """Add simple quantitative features used by the trading strategies."""
    result = df.copy()

    result["daily_return"] = result["close"].pct_change()
    result["cumulative_return"] = (1 + result["daily_return"].fillna(0)).cumprod() - 1
    result["ma_short"] = result["close"].rolling(window=short_window).mean()
    result["ma_long"] = result["close"].rolling(window=long_window).mean()
    result["momentum"] = result["close"] - result["close"].shift(momentum_window)
    result["rolling_volatility"] = (
        result["daily_return"].rolling(window=volatility_window).std()
    )

    return result
