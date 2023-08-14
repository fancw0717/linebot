import requests
from bs4 import BeautifulSoup

def get_latest_news():
    domain = 'https://168.motc.gov.tw'
    target_url = 'https://168.motc.gov.tw/theme/news'
    res = requests.get(target_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    news_items = soup.select('.news_content .table .tr')
    latest_news = []

    for item in news_items[1:6]:
        news_date = item.find(class_='td').text
        news_title = item.select('.td:nth-child(2) a')[0].text
        news_link = domain + item.select('.td:nth-child(2) a')[0]['href']
        
        news_info = f"日期：{news_date}\n標題：{news_title}\n連結：{news_link}\n"
        latest_news.append(news_info)
    
    return '\n\n'.join(latest_news)