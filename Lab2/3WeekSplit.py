"""
Написать скрипт, который разобъёт исходный csv файл на N файлов,
где каждый отдельный файл будет соответствовать одной неделе.
Файлы называются по первой и последней дате, которую они содержат.
"""

import csv


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
    # add to weeks n*7 rows
    for i in range(n):
        weeks.append(rows[i * 7:(i + 1) * 7])

    for i in range(n):
        print(f'Работаем с {weeks[i][0][0]}')
        week_data = weeks[i]
        first_date = week_data[0][0]
        first_date = first_date.replace('-', '')
        last_date = week_data[-1][0]
        last_date = last_date.replace('-', '')
        print(f'Первая дата: {first_date}, последняя дата: {last_date}')
        with open(f'data/{first_date}_{last_date}.csv', 'w+', encoding='utf8') as week_file:
            writer = csv.writer(week_file)
            writer.writerow(['data', 'temperature', 'pressure', 'wind'])
            for row in week_data:
                writer.writerow(row)
            week_file.close()


if __name__ == "__main__":
    split_by_week_n('data/dataset.csv', 5)
