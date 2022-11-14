from bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime


def write_table(url_from, file, year, month):
    """Функция write_table(html, file) записывает определенную таблицу с html сайта в file.csv файл"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    html = requests.get(f'{url_from}/{year}/{month}', headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    writer = csv.writer(file)
    for row in soup.select('div[id="data_block"]>table>tbody:last-child>tr'):
        children = list(row.select('td'))

        year = int(year)
        month = int(month)
        day = int("".join([c.text for c in children[0]]))
        date = datetime(year, month, day)

        line = [date.strftime('%Y-%m-%d')] + [c.text for c in children[1:3] + [children[5]]]

        writer.writerow(line)


def table_to_csv(filename, url_from, year, month):
    """
    Функция table_to_csv(filename, url, year, month) создает таблицу с именем
    filename, записывает в нее таблицу из url, с даты указанной даты year.month
    """
    with open(filename, 'w+', encoding='utf8') as dataset:
        print(f'File generated: {datetime.today()}', file=dataset)
        print('data,temperature,pressure,wind', file=dataset)

        today_year = datetime.now().timetuple().tm_year
        today_month = datetime.now().timetuple().tm_mon

        while year <= today_year:
            while month <= 12:
                if year == today_year and month == today_month:
                    print('Reached the current date')
                    break
                write_table(url_from, dataset, year, month)

                month += 1
            year += 1
            month = 1


if __name__ == "__main__":
    start = datetime.now().timestamp()

    url = 'https://www.gismeteo.ru/diary/4618'

    min_year = 2008
    min_month = 1

    table_to_csv('../Lab2/data/dataset.csv', url, min_year, min_month)

    end = datetime.now().timestamp()
    print(f'Scraping task finished in {round(end - start, 2)} sec')
