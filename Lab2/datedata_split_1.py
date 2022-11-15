import csv


def split_by_date_data(output: str, filename: str):
    """
    Функция split_by_date_data(output, filename) разбивает исходный csv файл на два с одинаковым количеством строк.
    Первый файл будет содержать даты, второй - данные.
    Параметр output - имя файла, в который будет записан результат.
    Параметр filename - имя файла, который будет разбит.
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        next(reader)
        rows = list(reader)

    with open(f'{output}X.csv', 'w+', encoding='utf8') as dates:
        writer = csv.writer(dates)
        for row in rows:
            writer.writerow([row[0]])

    with open(f'{output}Y.csv', 'w+', encoding='utf8') as data:
        writer = csv.writer(data)
        for row in rows:
            writer.writerow(row[1:])


if __name__ == "__main__":
    split_by_date_data('../data/', '../data/dataset.csv')
