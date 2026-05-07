from pathlib import Path

import matplotlib

# Use a non-interactive backend so plots save correctly in headless environments.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


PERCENT_METRICS = {
    "total_return",
    "annualized_return",
    "annualized_volatility",
    "max_drawdown",
}


def plot_equity_curves(
    strategy_results: dict[str, pd.DataFrame],
    output_path: str | Path,
) -> None:
    """Save an equity curve comparison plot."""
    output = Path(output_path)

    plt.figure(figsize=(10, 6))
    for strategy_name, result in strategy_results.items():
        plt.plot(result["date"], result["portfolio_value"], label=strategy_name)

    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.title("Equity Curve Comparison")
    plt.legend()
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def plot_metric_comparison(summary_df: pd.DataFrame, output_path: str | Path) -> None:
    """Save a bar chart comparing important performance metrics."""
    output = Path(output_path)
    metrics_to_plot = [
        "total_return",
        "annualized_return",
        "sharpe_ratio",
        "max_drawdown",
    ]
    plot_df = summary_df.set_index("strategy")[metrics_to_plot].copy()

    for metric in metrics_to_plot:
        if metric in PERCENT_METRICS:
            plot_df[metric] = plot_df[metric] * 100

    ax = plot_df.plot(kind="bar", figsize=(10, 6))
    ax.set_title("Performance Metric Comparison")
    ax.set_xlabel("Strategy")
    ax.set_ylabel("Value (returns and drawdown shown as %)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()
