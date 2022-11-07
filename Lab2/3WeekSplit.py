"""
Написать скрипт, который разобъёт исходный csv файл на N файлов,
где каждый отдельный файл будет соответствовать одной неделе.
Файлы называются по первой и последней дате, которую они содержат.
"""

import csv
from datetime import datetime, timedelta


def split_by_week_n(filename, n):
    """
    Функция split_by_week_n(filename, n) разбивает файл filename на n файлов
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)
        # delete 2 first rows
        rows = rows[2:]
        dataset.close()

    weeks = []
    for row in rows:
        weeks.append(datetime.strptime(row[0], '%Y-%m-%d'))

    weeks = list(set(weeks))
    weeks.sort()

    for i in range(0, len(weeks), n):
        with open(f'{weeks[i].strftime("%Y-%m-%d")}-{(weeks[i+n-1] + timedelta(days=7)).strftime("%Y-%m-%d")}.csv', 'w+', encoding='utf8') as week_n:
            writer = csv.writer(week_n)
            for row in rows:
                if weeks[i] <= datetime.strptime(row[0], '%Y-%m-%d') <= weeks[i+n-1]:
                    writer.writerow(row)
            week_n.close()


if __name__ == "__main__":
    split_by_week_n('data/dataset.csv', 5)
