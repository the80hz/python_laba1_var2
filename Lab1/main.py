import time
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree
import csv
import requests

start = time.time()

headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
           }

_url_samara_ = 'https://www.gismeteo.ru/diary/4618/'

_today_year_ = datetime.now().timetuple().tm_year
_today_month_ = datetime.now().timetuple().tm_mon

year = 2008
month = 1

database = open('dataset.csv', 'w+')
database.write('File generated: ' + str(datetime.today()) + '\n')
database.write('data,temperature,pressure,wind \n')

while year <= _today_year_:
    while month <= 12:
        if year == _today_year_ and month == _today_month_:
            print('Reached the current date')
            break

        url = _url_samara_ + str(year) + '/' + str(month) + '/'
        print(url)
        page = requests.get(url, headers=headers)

        writer = csv.writer(database)

        soup = BeautifulSoup(page.text, "lxml")

        dom = etree.HTML(str(soup))
        res = dom.xpath('//*[@id="data_block"]/table')[0].findall('tr')
        data = list()

        print(res)
        for row in res:
            data.append([c.text for c in row.getchildren()])
            writer.writerow(data)

        month += 1
    year += 1
    month = 1

print('Scraping task finished')
end = time.time()
print(str(round(end - start, 2)) + 'sec')
