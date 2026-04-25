def make_ma_crossover_signals(df):
    """
    Buy when the short moving average is above the long moving average.
    Otherwise stay out.
    """
    df = df.copy()
    df["signal"] = 0
    df.loc[df["ma_short"] > df["ma_long"], "signal"] = 1
    return df
