import pandas as pd

from src.metrics import calculate_metrics


def test_calculate_metrics_returns_expected_keys():
    df = pd.DataFrame(
        {
            "strategy_return": [0.0, 0.01, -0.02],
            "portfolio_value": [1000.0, 1010.0, 989.8],
        }
    )

    metrics = calculate_metrics(df)

    assert "total_return" in metrics
    assert "annualized_return" in metrics
    assert "annualized_volatility" in metrics
    assert "sharpe_ratio" in metrics
    assert "max_drawdown" in metrics
