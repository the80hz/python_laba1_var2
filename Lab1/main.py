import os
from bs4 import BeautifulSoup
import time
import requests
from datetime import datetime

start = time.time()

url_samara = 'https://www.gismeteo.ru/diary/4618/'


today_year = datetime.now().timetuple().tm_year
today_month = datetime.now().timetuple().tm_mon

year = 2008
month = 1

#while month <= 2022:

print("Scraping task finished")
end = time.time()
print(str(round(end - start, 2)) + 'sec')
