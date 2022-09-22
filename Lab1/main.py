import os
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup


start = time.time()

_url_samara_ = 'https://www.gismeteo.ru/diary/4618/'

_today_year_ = datetime.now().timetuple().tm_year
_today_month_ = datetime.now().timetuple().tm_mon

year = 2008
month = 1

database = open('dataset.csv', 'w+')

while year <= _today_year_:
    while month <= 12:
        if year == _today_year_ and month == _today_month_:
            print('Reached the current date')
            break
        url = _url_samara_ + str(year) + '/' + str(month)
        request_go = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})


        month += 1
    year += 1
    month = 1

print('Scraping task finished')
end = time.time()
print(str(round(end - start, 2)) + 'sec')
