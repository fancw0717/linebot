import requests
from bs4 import BeautifulSoup

def get_motor_ptt():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'html.parser')
    tags = soup.find_all(class_='title')[:7]
    content_list = []

    for tag in tags:
        title = tag.text.strip()
        
        a_tag = tag.find('a')
        href = a_tag['href'] if a_tag else None
        if not href:
            continue  # 如果找不到連結，則跳過此次循環
        
        meta_div = tag.find_next('div', class_='meta')
        if not meta_div:
            continue
        
        date_tag = meta_div.find('div', class_='date')
        date = date_tag.text.strip() if date_tag else "未知日期"
        
        content = f"日期: {date}\n標題: {title}\n連結: https://www.ptt.cc{href}\n"
        content_list.append(content)

    return content_list

