import csv
import os


def split_by_year_n(output, filename, n):
    """
    Функция split_by_year_n(output, filename, n) разбивает файл filename на n файлов по годам.
    Параметр output - имя файла, в который будет записан результат.
    Параметр filename - имя файла, который будет разбит.
    Параметр n - количество файлов, на которые будет разбит исходный файл.
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        rows = list(reader)
        rows = rows[2:]

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
        path = os.path.join(output, f'{first_date}_{last_date}.csv')
        with open(path, 'w+', encoding='utf8') as year_file:
            writer = csv.writer(year_file)
            writer.writerow(['data', 'temperature', 'pressure', 'wind'])
            for row in year_data:
                writer.writerow(row)


if __name__ == "__main__":
    split_by_year_n('data/', 'data/dataset.csv', 3)
