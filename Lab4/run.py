import pandas as pd


def temperature_filter(_df: pd, temp: float) -> pd:
    """
    Filter by temperature and return dataframe
    """
    return _df[_df["Temperature"] >= temp]


def date_filter(_df: pd, _start: str, _end: str) -> pd:
    """
    Filter by date and return dataframe
    """
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    return _df.loc[(_df["Date"] >= _start) & (_df["Date"] <= _end)]


def group_by_date(_df: pd):
    """
    Group by date and return dataframe
    """
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    return _df.groupby(_df["Date"].dt.month)[
        "Temperature",
        "Fahrenheit",
    ].mean()


def dataframe(path: str) -> pd:
    """
    Read csv file and return pandas dataframe
    """
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
