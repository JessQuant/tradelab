def make_buy_and_hold_signals(df):
    """
    Always stay invested.
    """
    df = df.copy()
    df["signal"] = 1
    return df
