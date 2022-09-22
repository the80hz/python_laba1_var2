import requests
from datetime import datetime

HEADERS = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.0.0 Safari/537.36 "
}

_url_samara_ = 'https://www.gismeteo.ru/diary/4618/'

_today_year_ = datetime.now().timetuple().tm_year
_today_month_ = datetime.now().timetuple().tm_mon

year = 2008
month = 1


url = _url_samara_ + str(year) + '/' + str(month) + '/'

req = requests.get(url, headers=HEADERS)
