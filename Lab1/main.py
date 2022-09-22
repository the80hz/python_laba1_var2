import os
import time
import requests
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup

def get_content(_html):
    soup = BeautifulSoup(_html, 'html.parser')
    #for item in soup.find_all('td')




start = time.time()

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
        url = _url_samara_ + str(year) + '/' + str(month)
        html_site = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        #list =


        month += 1
    year += 1
    month = 1

print('Scraping task finished')
end = time.time()
print(str(round(end - start, 2)) + 'sec')
