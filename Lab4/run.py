import pandas as pd


def dataframe(path: str) -> pd:
    _df = pd.read_csv(path, sep=",")
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")

    return _df


if __name__ == "__main__":
    df = dataframe('../data/dataset.csv')
