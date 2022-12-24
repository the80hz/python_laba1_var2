import pandas as pd
import matplotlib.pyplot as plt


def graphics(_df: pd) -> None:
    """
    graphics(_df: pd) -> None
    _df: pandas dataframe

    Draws graphs of temperature changes
    """
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(40, 8))
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    axes[0].bar(_df["Date"], _df["Temperature"], color="#5900A6")
    axes[0].set(title="Temperature")
    axes[0].set_xlabel("date")
    axes[0].set_ylabel("temp")

    plt.show()


def graphics_date(_df: pd, month: int, year: int):
    """
    graphics_date(_df: pd, month: int, year: int) -> None
    _df: pandas dataframe
    month: the desired month
    year: the desired year

    Draws graphs of temperature changes by date
    """
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(40, 8))
    tmp_df = _df.loc[(_df["Date"].dt.year == year) & (_df["Date"].dt.month == month)]
    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    axes[0].plot(tmp_df["Date"], tmp_df["Temperature"], color="#5900A6")
    axes[0].set(title="Temperature")
    axes[0].set_xlabel("date")
    axes[0].set_ylabel("temp")

    axes[1].plot(
        tmp_df["Date"],
        tmp_df["Temperature"].rolling(20).median(),
        color="#5900A6",
    )
    axes[1].set(title="Median")
    axes[1].set_xlabel("date")
    axes[1].set_ylabel("temp")

    axes[2].plot(
        tmp_df["Date"], tmp_df["Temperature"].rolling(20).mean(), color="#5900A6"
    )
    axes[2].set(title="Mean")
    axes[2].set_xlabel("date")
    axes[2].set_ylabel("temp")

    plt.show()


def temperature_filter(_df: pd, temp: float) -> pd:
    """
    temperature_filter(_df: pd, temp: float) -> pd
    _df: pandas dataframe
    temp: the desired temperature

    Filter by temperature and return dataframe
    """
    return _df[_df["Temperature"] >= temp]


def date_filter(_df: pd, _start: str, _end: str) -> pd:
    """
    date_filter(_df: pd, _start: str, _end: str) -> pd
    _df: pandas dataframe
    _start: start date
    _end: end date

    Filter by date and return dataframe
    """
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    return _df.loc[(_df["Date"] >= _start) & (_df["Date"] <= _end)]


def group_by_date(_df: pd):
    """
    group_by_date(_df: pd) -> pd
    _df: pandas dataframe

    Group by date and return dataframe
    """
    _df["Date"] = pd.to_datetime(_df["Date"], format="%Y-%m-%d")
    return _df.groupby(_df["Date"].dt.month)[
        "Temperature",
        "Fahrenheit",
    ].mean()


def statistics(_df: pd) -> None:
    """
    statistics(_df: pd) -> None
    _df: pandas dataframe

    Print statistics
    """
    print(
        _df["Temperature"].describe(),
        _df["Fahrenheit"].describe(),
    )


def dataframe(path: str) -> pd:
    """
    dataframe(path: str) -> pd
    path: path to file

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

    temperature_filter(df, 21)
    statistics(df)

    graphics(df)
    graphics_date(df, 7, 2011)
