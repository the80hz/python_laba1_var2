"""
Написать скрипт, содержащий функцию, принимающую на вход дату (тип datetime) и возвращающий данные для этой даты (из файла) или None если данных для этой даты нет.
Функция должна быть представлена в четырёх версиях в зависимости от типа входных файлов, из которых будут прочитаны данные (пункты 0–3).
Написать функцию next(), которая будет при первом вызове возвращать данные для самой ранней возможной даты (возвращается кортеж (дата, данные)), а при каждом следующем вызове данные для следующей по порядку даты.
Если попадается дата, для которой данные отсутствуют, то она игнорируется и возвращаются данные для следующей валидной даты.
"""

from datetime import datetime
import csv
import os
from re import search


def search_with_date(date: datetime, filename):
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)
        rows = rows[2:]
        dataset.close()

    for row in rows:
        if row[0] == date.strftime('%Y-%m-%d'):
            return row[1:]
    return None


def search_with_file(x, filename):
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        date_data = list(reader)
        date_data = date_data[2:]
        dataset.close()

    with open(x, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        date = list(reader)
        date = date[1:]
        file.close()

    data = []
    for row in date:
        for row2 in date_data:
            if row[0] == row2[0]:
                data.append(row2[1:])

    if not data:
        return None
    return data


def next(filename):
    if not os.path.exists(f'{filename}.temp'):
        with open(filename, 'r', encoding='utf8') as dataset:
            reader = csv.reader(dataset)
            date_data = list(reader)
            date_data = date_data[2:]
            dataset.close()
            date_data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
            with open(f'{filename}.temp', 'w', encoding='utf8') as file:
                writer = csv.writer(file)
                writer.writerows(date_data)
                file.close()

    with open(f'{filename}.temp', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        data = list(reader)
        file.close()

    temp = data[0]

    # delete first row in file
    with open(f'{filename}.temp', 'w', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerows(data[1:])
        file.close()

    return temp


if __name__ == "__main__":
    csv_name = 'data/dataset.csv'
    print(search_with_date(datetime(2020, 1, 1), 'data/dataset.csv'))
    print(search_with_file('data/20080207_20080213.csv', 'data/dataset.csv'))
    print(next(csv_name))
    print(next(csv_name))
    print(next(csv_name))

    os.remove(f'{csv_name}.temp')
