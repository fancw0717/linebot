import requests
from bs4 import BeautifulSoup

def get_motor_ptt():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    tags = soup.find_all(class_='title')[:5]
    
    for tag in tags :
        title = tag.text
        href = tag.find('a')['href']  # 获取<a>标签中的href属性
        content = f"標題: {title}\n連結: https://www.ptt.cc{href}\n"
    return content