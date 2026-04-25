import pandas as pd

from src.strategies.buy_and_hold import make_buy_and_hold_signals
from src.strategies.ma_crossover import make_ma_crossover_signals


def test_buy_and_hold_signals_are_all_one():
    df = pd.DataFrame({"close": [100, 101, 102]})
    result = make_buy_and_hold_signals(df)
    assert list(result["signal"]) == [1, 1, 1]


def test_ma_crossover_signals():
    df = pd.DataFrame(
        {
            "ma_short": [1, 3, 2],
            "ma_long": [2, 2, 2],
        }
    )

    result = make_ma_crossover_signals(df)

    assert list(result["signal"]) == [0, 1, 0]
