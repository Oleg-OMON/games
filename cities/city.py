import json
from bs4 import BeautifulSoup
import requests

city_list = []

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, '
                             'like Gecko) Version/13.1 Safari/605.1.15'}

    # req = requests.get(url, headers=headers)
    #
    # with open('russia_city.html', 'w') as file:
    #     file.write(req.text)

    with open('russia_city.html', ) as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    city_all = soup.find_all('table')
    for item in city_all:
        city = item.find_all('tr')[1:]

        for i in city:
            dic = {}
            c = i.find('td').text
            city_list.append(c)

        # print(city_list)


get_data('https://33tura.ru/goroda-rossii')


