import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_price_data
from src.cleaner import clean_price_data
from src.features import add_features
from src.backtester import run_backtest
from src.metrics import calculate_metrics
from src.strategies.buy_and_hold import make_buy_and_hold_signals
from src.strategies.ma_crossover import make_ma_crossover_signals


def main():
    filepath = "data/sample_prices.csv"
    initial_cash = 1000.0

    # Load and prepare the data
    df = load_price_data(filepath)
    df = clean_price_data(df)
    df = add_features(df)

    # Strategy 1: Buy and Hold
    buy_hold_df = make_buy_and_hold_signals(df)
    buy_hold_results = run_backtest(buy_hold_df, initial_cash=initial_cash)
    buy_hold_metrics = calculate_metrics(buy_hold_results, initial_cash=initial_cash)

    # Strategy 2: Moving Average Crossover
    ma_df = make_ma_crossover_signals(df)
    ma_results = run_backtest(ma_df, initial_cash=initial_cash)
    ma_metrics = calculate_metrics(ma_results, initial_cash=initial_cash)

    # Compare results
    summary = pd.DataFrame(
        [
            {"strategy": "Buy and Hold", **buy_hold_metrics},
            {"strategy": "MA Crossover", **ma_metrics},
        ]
    )

    print("\nPerformance summary:\n")
    print(summary)

    # Save result tables
    buy_hold_results.to_csv("data/buy_hold_results.csv", index=False)
    ma_results.to_csv("data/ma_crossover_results.csv", index=False)
    summary.to_csv("data/performance_summary.csv", index=False)

    # Plot equity curves
    plt.figure(figsize=(10, 6))
    plt.plot(buy_hold_results["date"], buy_hold_results["portfolio_value"], label="Buy and Hold")
    plt.plot(ma_results["date"], ma_results["portfolio_value"], label="MA Crossover")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.title("Equity Curve Comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data/equity_curve.png")
    plt.show()

    print("\nSaved:")
    print("- data/buy_hold_results.csv")
    print("- data/ma_crossover_results.csv")
    print("- data/performance_summary.csv")
    print("- data/equity_curve.png")


if __name__ == "__main__":
    main()
