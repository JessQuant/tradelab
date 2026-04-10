from src.data_loader import load_price_data


def test_load_price_data():
    df = load_price_data("data/sample_prices.csv")
    assert "close" in df.columns
    assert len(df) > 0
