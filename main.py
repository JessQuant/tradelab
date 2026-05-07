from argparse import ArgumentParser
from pathlib import Path

import pandas as pd

from src.backtester import run_backtest
from src.cleaner import clean_price_data
from src.data_loader import load_price_data
from src.features import add_features
from src.metrics import calculate_metrics
from src.plotting import plot_equity_curves, plot_metric_comparison
from src.strategies.buy_and_hold import make_buy_and_hold_signals
from src.strategies.ma_crossover import make_ma_crossover_signals


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Run the tradelab backtesting pipeline.")
    parser.add_argument(
        "--input",
        default="data/sample_prices.csv",
        help="Path to the input CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory where output files will be saved.",
    )
    parser.add_argument(
        "--initial-cash",
        type=float,
        default=10000.0,
        help="Starting portfolio value for each strategy.",
    )
    parser.add_argument(
        "--transaction-cost",
        type=float,
        default=0.001,
        help="Transaction cost charged when position changes.",
    )
    return parser


def run_pipeline(
    input_path: str,
    output_dir: str,
    initial_cash: float,
    transaction_cost: float,
) -> pd.DataFrame:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load and prepare data
    df = load_price_data(input_path)
    df = clean_price_data(df)
    df = add_features(df)
    df.to_csv(output_path / "processed_prices.csv", index=False)

    strategy_builders = {
        "Buy and Hold": make_buy_and_hold_signals,
        "MA Crossover": make_ma_crossover_signals,
    }

    strategy_results = {}
    summary_rows = []

    for strategy_name, signal_builder in strategy_builders.items():
        strategy_df = signal_builder(df)

        result = run_backtest(
            strategy_df,
            initial_cash=initial_cash,
            transaction_cost=transaction_cost,
        )

        metrics = calculate_metrics(result, initial_cash=initial_cash)

        safe_name = strategy_name.lower().replace(" ", "_")
        result.to_csv(output_path / f"{safe_name}_results.csv", index=False)

        strategy_results[strategy_name] = result
        summary_rows.append({"strategy": strategy_name, **metrics})

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(output_path / "performance_summary.csv", index=False)

    plot_equity_curves(strategy_results, output_path / "equity_curve.png")
    plot_metric_comparison(summary_df, output_path / "metric_comparison.png")

    print("\nPerformance summary:\n")
    print(summary_df.round(4))
    print(f"\nSaved files to {output_path}")

    return summary_df


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    run_pipeline(
        input_path=args.input,
        output_dir=args.output_dir,
        initial_cash=args.initial_cash,
        transaction_cost=args.transaction_cost,
    )


if __name__ == "__main__":
    main()
