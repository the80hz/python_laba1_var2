import csv


def split_by_date_data(filename):
    """
    Функция split_by_date_data(filename) разбивает исходный csv файл на два с одинаковым количеством строк.
    Первый файл будет содержать даты, второй - данные.
    """
    with open(filename, 'r', encoding='utf8') as dataset:
        reader = csv.reader(dataset)
        next(reader)
        rows = list(reader)
        dataset.close()

    with open('dates.csv', 'w+', encoding='utf8') as dates:
        writer = csv.writer(dates)
        for row in rows:
            writer.writerow([row[0]])
        dates.close()

    with open('data.csv', 'w+', encoding='utf8') as data:
        writer = csv.writer(data)
        for row in rows:
            writer.writerow(row[1:])
        data.close()


if __name__ == "__main__":
    split_by_date_data('dataset.csv')
