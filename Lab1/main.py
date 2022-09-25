from datetime import datetime
from bs4 import BeautifulSoup
import csv
import requests

URL = 'https://www.gismeteo.ru/diary/4618'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

start = datetime.now().timestamp()
YEAR = datetime.now().timetuple().tm_year
MONTH = datetime.now().timetuple().tm_mon


def request(url):
    return requests.get(url, headers=HEADERS)


def write_table(html, file):
    soup = BeautifulSoup(html.text, 'html.parser')

    writer = csv.writer(dataset)
    for row in soup.select('div[id="data_block"]>table>tbody:last-child>tr'):
        children = list(row.select('td'))

        num = ([c.text for c in children[0]])
        y = ''.join(num)

        date = [f'{year}.{month}.{str(y)}']
        line = date + [c.text for c in children[1:3] + [children[5]]]

        writer.writerow(line)


if __name__ == "__main__":
    with open('dataset.csv', 'w+', encoding='utf8') as dataset:
        print(f'File generated: {datetime.today()}', file=dataset)
        print('data,temperature,pressure,wind', file=dataset)
        year = 2008
        month = 1

        while year <= YEAR:
            while month <= 12:
                if year == YEAR and month == MONTH:
                    print('Reached the current date')
                    break

                page = request(f'{URL}/{year}/{month}')
                write_table(page, dataset)

                month += 1
            year += 1
            month = 1

        dataset.close()

    end = datetime.now().timestamp()
    print(f'Scraping task finished in {round(end - start, 2)} sec')

