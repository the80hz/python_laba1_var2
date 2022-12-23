import pandas as pd


def dataframe(path: str) -> pd:
    _df = pd.read_csv(path, sep=",")
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    _df.fillna(
        {
            "Temperature": _df["Temperature"].mean(),
            "Pressure": "no data",
            "Wind": "no data",
        },
        inplace=True,
    )

    _df["Fahrenheit"] = _df["Temperature"] * 1.8 + 32
    return _df


if __name__ == "__main__":
    df = dataframe('../data/dataset.csv')
