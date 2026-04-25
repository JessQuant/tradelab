# tradelab

This repo is for my final project.

I’m making a simple Python backtesting project for trading strategies. The basic idea is to use historical market data, test a couple of simple strategies on it, and compare the results to buy-and-hold.

## Project aims

- load price data
- clean the data
- calculate a few simple indicators
- generate buy and sell signals
- backtest the strategy
- compare performance
- calculate basic performance metrics
- produce an equity curve plot

## Strategies

- Buy and Hold
- Moving Average Crossover

## Languages and libraries

- Python
- pandas
- numpy
- matplotlib
- pytest

## Current project structure

- `data/sample_prices.csv` - sample input data
- `data/processed_sample_prices.csv` - processed output data
- `src/data_loader.py` - loads and validates the CSV data
- `src/cleaner.py` - cleans the dataset
- `src/features.py` - adds features such as returns, moving averages, and momentum
- `src/strategies/buy_and_hold.py` - creates buy-and-hold signals
- `src/strategies/ma_crossover.py` - creates moving average crossover signals
- `src/backtester.py` - runs the backtest
- `src/metrics.py` - calculates performance metrics
- `main.py` - runs the full pipeline
- `tests/test_loader.py` - basic test for the data loader

## What the project does right now

Right now, the project can:

- load historical price data from a CSV file
- clean and sort the data
- calculate simple features
- generate strategy signals
- run a simple backtest
- calculate metrics such as return, volatility, Sharpe ratio, and drawdown
- save output files
- produce a simple equity curve plot

## How to run the code

From the top-level project folder, run:

```bash
python3 main.py