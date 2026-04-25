import pandas as pd

from src.backtester import run_backtest


def test_run_backtest_creates_output_columns():
    df = pd.DataFrame(
        {
            "daily_return": [0.0, 0.01, -0.02],
            "signal": [1, 1, 0],
        }
    )

    result = run_backtest(df)

    assert "position" in result.columns
    assert "trade" in result.columns
    assert "strategy_return" in result.columns
    assert "portfolio_value" in result.columns
    assert result["portfolio_value"].iloc[0] == 1000.0
