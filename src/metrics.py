import numpy as np


def calculate_metrics(df, initial_cash=1000.0):
    """
    Calculate simple backtest performance metrics.
    """
    returns = df["strategy_return"].dropna()
    portfolio = df["portfolio_value"]

    if len(returns) == 0:
        return {
            "total_return": np.nan,
            "annualized_return": np.nan,
            "annualized_volatility": np.nan,
            "sharpe_ratio": np.nan,
            "max_drawdown": np.nan,
        }

    total_return = portfolio.iloc[-1] / initial_cash - 1

    annualized_return = (portfolio.iloc[-1] / initial_cash) ** (252 / len(returns)) - 1
    annualized_volatility = returns.std(ddof=0) * np.sqrt(252)

    if returns.std(ddof=0) == 0:
        sharpe_ratio = np.nan
    else:
        sharpe_ratio = (returns.mean() / returns.std(ddof=0)) * np.sqrt(252)

    running_max = portfolio.cummax()
    drawdown = portfolio / running_max - 1
    max_drawdown = drawdown.min()

    return {
        "total_return": total_return,
        "annualized_return": annualized_return,
        "annualized_volatility": annualized_volatility,
        "sharpe_ratio": sharpe_ratio,
        "max_drawdown": max_drawdown,
    }
