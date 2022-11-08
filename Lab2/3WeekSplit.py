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
        rows = rows[2:]
        dataset.close()

    weeks = []
    # every 7 rows append to weeks

    print(weeks)




if __name__ == "__main__":
    split_by_week_n('data/dataset.csv', 5)
