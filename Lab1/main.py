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
TODAY_YEAR = datetime.now().timetuple().tm_year
TODAY_MONTH = datetime.now().timetuple().tm_mon

year = 2008
month = 1

with open('dataset.csv', 'w+', encoding='utf8') as database:
    print(f'File generated: {datetime.today()}', file=database)
    print('data,temperature,pressure,wind', file=database)

    while year <= TODAY_YEAR:
        while month <= 12:
            if year == TODAY_YEAR and month == TODAY_MONTH:
                print('Reached the current date')
                break

            page = requests.get(f'{URL}/{year}/{month}', headers=HEADERS)
            soup = BeautifulSoup(page.text, 'html.parser')

            writer = csv.writer(database)
            for row in soup.select('div[id="data_block"]>table>tbody:last-child>tr'):
                children = list(row.select('td'))

                num = ([c.text for c in children[0]])
                y = ''.join(num)

                date = [f'{year}.{month}.{str(y)}']
                line = date + [c.text for c in children[1:3] + [children[5]]]

                writer.writerow(line)
            month += 1
        year += 1
        month = 1

    database.close()

end = datetime.now().timestamp()
print(f'Scraping task finished in {round(end - start, 2)} sec')
