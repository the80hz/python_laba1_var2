import csv
import os
from datetime import datetime


def search_with_date(date: datetime, filename: str):
    """
    Функция search_with_date(date, filename) ищет в файле filename данные по datetime.
    Если данных нет, то возвращает None.
    Параметр date - дата, в формате datetime, по которой будет производиться поиск.
    Параметр filename - имя файла, в котором будет производиться поиск.
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)
        rows = rows[2:]

    for row in rows:
        if row[0] == date.strftime('%Y-%m-%d'):
            return row[1:]
    return None


def search_with_file(x:str, filename:str):
    """
    Функция search_with_file(x, filename) ищет в файле filename данные по дате из файла .csv.
    Если данных нет, то возвращает None.
    Параметр x - имя файла с датами, по которой будет производиться поиск.
    Параметр filename - имя файла, в котором будет производиться поиск.
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        date_data = list(reader)
        date_data = date_data[2:]

    with open(x, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        date = list(reader)
        date = date[1:]

    data = []
    for row in date:
        for row2 in date_data:
            if row[0] == row2[0]:
                data.append(row2[1:])

    if not data:
        return None
    return data


def next(filename: str):
    """
    Функция next(filename) возвращает данные для самой ранней возможной даты в файле filename
    Параметр filename - имя файла, в котором будет производиться поиск.
    """
    if not os.path.exists(f'{filename}.temp'):
        with open(filename, 'r', encoding='utf8') as dataset:
            reader = csv.reader(dataset)
            date_data = list(reader)
            date_data = date_data[2:]
            date_data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
            with open(f'{filename}.temp', 'w', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerows(date_data)

    with open(f'{filename}.temp', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        data = list(reader)

    temp = data[0]

    with open(f'{filename}.temp', 'w', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerows(data[1:])

    return temp[1:]


if __name__ == "__main__":
    csv_name = '../data/dataset.csv'
    print(search_with_date(datetime(2010, 1, 1), csv_name))
    print(search_with_file('../data/20080207_20080213.csv', csv_name))
    print(next(csv_name))
    print(next(csv_name))
    print(next(csv_name))

    os.remove(f'{csv_name}.temp')
