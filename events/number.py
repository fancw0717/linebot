import requests
from bs4 import BeautifulSoup

def get_motor_ptt():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    tags = soup.find_all(class_='title')
    for tag in range(min(5, len(tags))):
        title = tags[tag].find('a').text
        href = tags['href']  # 获取<a>标签中的href属性
        content = f"標題: {title}\n連結: https://www.ptt.cc{href}\n"
    return content