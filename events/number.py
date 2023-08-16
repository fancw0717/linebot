import requests
from bs4 import BeautifulSoup

def get_motor_ptt():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    tags = soup.find_all(class_='title')[:5]
    content_list = []  # 創建一個列表來保存標題和連結

    for tag in tags:
        title = tag.text
        href = tag.find('a')['href']  # 获取<a>标签中的href属性
        meta_div = tag.find_next('div', class_='meta')
        date_tag = meta_div.find('div', class_='date')  # 在meta信息中找到日期标签
        date = date_tag.text.strip()  # 获取日期文本并去除首尾空格
        content = f"日期: {date}\n標題: {title}\n連結: https://www.ptt.cc{href}\n"
        content_list.append(content)  # 將標題和連結添加到列表中

    return content_list