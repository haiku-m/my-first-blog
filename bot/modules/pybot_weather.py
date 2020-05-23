import requests
from bs4 import BeautifulSoup

def weather_command():
    res = requests.get('https://tenki.jp/forecast/2/10/3610/7205/')
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    telop = soup.find('p', class_ = 'weather-telop').get_text()
    temp = soup.find_all('span', class_='value')
    contens = []
    for i in temp:
        contens.append(i.text)
    high_temp = soup.find('dd', class_ = 'high-temp tempdiff').get_text()
    low_temp = soup.find('dd', class_ = 'low-temp tempdiff').get_text()
    response = f'白河市の天気は「{telop}」、最高は{contens[0]}℃{high_temp}、\
        最低は{contens[1]}℃{low_temp}です。'
    return response