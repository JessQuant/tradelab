def run_backtest(df, signal_col="signal", initial_cash=1000.0, transaction_cost=0.001):
    """
    Run a very simple backtest.

    signal = 1 means invested
    signal = 0 means in cash
    transaction_cost is charged when position changes
    """
    df = df.copy()

    # Fill the first missing return with 0
    df["daily_return"] = df["daily_return"].fillna(0)

    # Use yesterday's signal to avoid look-ahead bias
    df["position"] = df[signal_col].shift(1).fillna(0)

    # A trade happens when position changes
    df["trade"] = df["position"].diff().abs().fillna(df["position"].abs())

    # Strategy return = market return when invested - trading cost
    df["strategy_return"] = (
        df["position"] * df["daily_return"] - df["trade"] * transaction_cost
    )

    # Grow the portfolio over time
    df["portfolio_value"] = initial_cash * (1 + df["strategy_return"]).cumprod()

    return df
