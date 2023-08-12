import requests
from bs4 import BeautifulSoup
from line_bot_api import *

def bike_reply_other(stockNumber):
    content_text = "即時股價和K線圖"
    text_message = TextSendMessage(
                                text = content_text,
                                quick_reply = QuickReply(
                                    items=[
                                       QuickReplyButton(
                                                action = MessageAction(
                                                    label="# + 股票代號查詢",
                                                    text = "#"+stockNumber,
                                                )
                                       ),
                                       QuickReplyButton(
                                               action = MessageAction(
                                                    label="K線圖",
                                                    text = "@K"+stockNumber 
                                               )
                                       ),
                                        ]
                                ))
    return text_message

#油價查詢
def bike_info():
    target_url = 'https://autos.yahoo.com.tw/popular-bikes/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split('(')[0] #取名字
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content



# def oil_price():
#     target_url = 'https://gas.goodlife.tw/'
#     rs = requests.session()
#     res = rs.get(target_url, verify=False)
#     res.encoding = 'utf-8'
#     soup = BeautifulSoup(res.text, 'html.parser')
#     title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
#     gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
#     cpc = soup.select('#cpc')[0].text.replace(' ', '')
#     content = '{}\n{}{}'.format(title, gas_price, cpc)
#     return content