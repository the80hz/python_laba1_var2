"""
Скрипт, который разбивает исходный csv на N файлов, где каждый отдельный соответствует одному году.
Файлы называются по первой и последней дате, которую они содержат.
"""

import csv


def split_by_year_n(filename, n):
    """
    Функция split_by_year_n(filename, n) разбивает файл filename на n файлов
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)
        rows = rows[2:]
        dataset.close()

    years = []
    for row in rows:
        years.append(row[0][:4])
    years = list(set(years))
    years.sort()

    for i in range(0, n):
        print(f'Работаем с {years[i]}')
        year_data = []
        for row in rows:
            if row[0][:4] == years[i]:
                year_data.append(row)
        first_date = year_data[0][0]
        first_date = first_date.replace('-', '')
        last_date = year_data[-1][0]
        last_date = last_date.replace('-', '')
        print(f'Первая дата: {first_date}, последняя дата: {last_date}')
        with open(f'data/{first_date}_{last_date}.csv', 'w+', encoding='utf8') as year_file:
            writer = csv.writer(year_file)
            writer.writerow(['data', 'temperature', 'pressure', 'wind'])
            for row in year_data:
                writer.writerow(row)
            year_file.close()


if __name__ == "__main__":
    split_by_year_n('data/dataset.csv', 3)
