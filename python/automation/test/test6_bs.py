# 앞의 예제에서 text안에 html코드가 들어가있는데,
# 이 코드를 쉽게 다루기 위해서 bs가 필요함

import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    print(title)
else:
    print(response.status_code)


##########################################


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    print(ul)
else:
    print(response.status_code)


##########################################


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    titles = ul.select('li > dl > dt > a')
    for title in titles:
        print(title.get_text())
else : 
    print(response.status_code)