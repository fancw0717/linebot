import requests
from bs4 import BeautifulSoup

def get_motor_ptt():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    tags = soup.find_all(class_='title')
    tags = soup.find_all('div', class_='date')  
    content_list = []  # 創建一個列表來保存標題和連結

    for tag in tags[:5]:
        title = tag.text
        date = tags[tag].text.strip()  # 去除前後空白
        href = tag.find('a')['href']  # 获取<a>标签中的href属性
        content = f"標題: {title}\n連結: https://www.ptt.cc{href}\n {date}\n"
        content_list.append(content)  # 將標題和連結添加到列表中

    return content_list