"""
Скрипт, который разбивает исходный csv на N файлов, где каждый отдельный соответствует одному году.
Файлы называются по первой и последней дате, которую они содержат.
"""

import csv
from datetime import datetime


def split_by_year_n(filename, n):
    """
    Функция split_by_year_n(filename, n) разбивает файл filename на n файлов
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        next(reader)
        rows = list(reader)
        dataset.close()

    years = []
    for row in rows:
        years.append(datetime.strptime(row[0], '%Y-%m-%d').year)

    years = list(set(years))
    years.sort()

    for i in range(0, len(years), n):
        with open(f'{years[i]}-{years[i+n-1]}.csv', 'w+', encoding='utf8') as year_n:
            writer = csv.writer(year_n)
            for row in rows:
                if years[i] <= datetime.strptime(row[0], '%Y-%m-%d').year <= years[i+n-1]:
                    writer.writerow(row)
            year_n.close()


if __name__ == "__main__":
    split_by_year_n('dataset.csv', 5)
