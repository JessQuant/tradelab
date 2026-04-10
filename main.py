from src.data_loader import load_price_data
from src.cleaner import clean_price_data
from src.features import add_features


def main():
    filepath = "data/sample_prices.csv"

    df = load_price_data(filepath)
    df = clean_price_data(df)
    df = add_features(df)

    print("\nProcessed data:\n")
    print(df)

    df.to_csv("data/processed_sample_prices.csv", index=False)
    print("\nSaved processed file to data/processed_sample_prices.csv")


if __name__ == "__main__":
    main()
