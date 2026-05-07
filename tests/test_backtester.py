import pandas as pd


def run_backtest(
    df: pd.DataFrame,
    signal_col: str = "signal",
    initial_cash: float = 10000.0,
    transaction_cost: float = 0.001,
) -> pd.DataFrame:
    """Run a simple long-only backtest with transaction costs."""
    result = df.copy()

    if signal_col not in result.columns:
        raise ValueError(f"Missing signal column: {signal_col}")
    if "daily_return" not in result.columns:
        raise ValueError("Missing daily_return column")

    result["daily_return"] = result["daily_return"].fillna(0)
    result[signal_col] = result[signal_col].fillna(0).clip(0, 1)

    # Shift the signal by one day to avoid look-ahead bias.
    result["position"] = result[signal_col].shift(1).fillna(0)

    # A trade happens whenever the position changes.
    result["trade"] = result["position"].diff().abs().fillna(result["position"].abs())

    result["strategy_return"] = (
        result["position"] * result["daily_return"] - result["trade"] * transaction_cost
    )
    result["portfolio_value"] = initial_cash * (1 + result["strategy_return"]).cumprod()

    return result
