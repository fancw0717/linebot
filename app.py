#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.oil import *
from events.news import *
from events.Msg_Template import *
from events.EXRate import *
from events.map import *
from model.mongodb import *
import re
import twstock
import datetime
import flask
from bs4 import BeautifulSoup

app = Flask(__name__)

#抓使用者設定它關心的股票
def cache_users_stock():
    db = constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'stock'}))
        users.append(cel)
    return users

#監聽所有來自callback的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=LocationMessage)

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip() #使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱G
   
############################ 使用說明 選單 最新油價############################
    if message_text == '熊哥幫幫我':
        about_us_event(event)
    
    if message_text == '最新消息':
        news_content = get_latest_news()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=news_content)
        )

    if message_text == '附近資訊':
        google_map(event)  

#—————————————————————————————————————————————————————————————————————————————————
    # if event.message.text == '附近停車場':
    #     user_id = event.source.user_id
    #     api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

    #     user_location = f"{event.message.latitude},{event.message.longitude}"
    #     radius = 1000
    #     api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

    #     nearby_parking = search_nearby_parking(user_location, radius, api_key)
                
    #     if nearby_parking:
    #         reply_text = '附近的停車場有：\n'
    #         for parking in nearby_parking:
    #             name = parking['name']
    #             address = parking['vicinity']
    #             reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
    #     else:
    #         reply_text = '附近沒有找到停車場。'

    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextMessage(text=reply_text)
    #     )

    if event.message.text == '當前位置':
        latitude = event.message.latitude
        longitude = event.message.longitude
        map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        reply_message = TextSendMessage(text=f"您的位置：{map_url}")
        line_bot_api.reply_message(event.reply_token, reply_message)

    if event.message.text == '附近停車場':
        user_id = event.source.user_id
        api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

        user_location = f"{latitude},{longitude}"
        if user_location:
            radius = 1000

            nearby_parking = search_nearby_parking(user_location, radius, api_key)
            
            if nearby_parking:
                reply_text = '附近的停車場有：\n'
                for parking in nearby_parking:
                    name = parking['name']
                    address = parking['vicinity']
                    reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
            else:
                reply_text = '附近沒有找到停車場。'
        else:
            reply_text = '無法獲取您的地理位置。'

        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=reply_text)
        )

#—————————————————————————————————————————————————————————————————————————————————

    if event.message.text == "想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        
    if message_text == '速克達':
        flex_message = show_bk1_Button()  # 使用 show_sk1_Button() 來取得 Flex Message 物件
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)
        
    if message_text == '跑車':
        flex_message = show_bk2_Button()
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)

    if message_text == '街車':
        flex_message = show_bk3_Button()
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)

    if message_text == '美式機車':
        flex_message = show_bk4_Button()
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)

    if message_text == '越野車':
        flex_message = show_bk5_Button()
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)

    if message_text == '休旅車':
        flex_message = show_bk6_Button()
        line_bot_api.reply_message(
            event.reply_token,
            flex_message)       
    
        
############################ 使用說明 選單 股票看板 ############################
    if event.message.text == "股價查詢":
        line_bot_api.push_message(uid, TextSendMessage("請輸入#加股票代號...."))
    
    #股價查詢
    if re.match("我想看機車", msg):
        stockNumber = msg[5:]
        # = msg[5:]
        btn_msg = stock_reply_other(stockNumber)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    

    
    #新增使用者關注的股票到mongodb
    if re.match('關注[0-9]{4}[<>][0-9]', msg): #使用者新增股票至股票清單
        stockNumber = msg[2:]
        line_bot_api.push_message(uid, TextSendMessage("加入股票代號"+stockNumber))
        content = write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    

    #查詢股票篩選條件清單
    if re.match('股票清單', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下,股票查詢中...'))
        content = show_stock_setting(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0    #可以不用寫這行
    
    #刪除存在資料庫裏面的股票
    if re.match('刪除[0-9]{4}', msg):
        content = delete_my_stock(user_name, msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(Content))
        return 0
    
    #清空存在資料庫裏面的股票
    if re.match('清空股票', msg):
        content = delete_my_allstock(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(Content))
        return 0
    
    # else:
    #     content = write_my_stock(uid, user_name, stockNumber, "未設定", "未設定")
    #     line_bot_api.push_message(uid, TextSendMessage(content))
    #     return 0

    if(emsg.startswith('#')):
            text = emsg[1:]
            content = ''

            stock_rt = twstock.realtime.get(text)
            my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
            my_time = my_datetime.strftime('%H:%M:%S')

            content += '%s (%s) %s\n' %(
                stock_rt['info']['name'],
                stock_rt['info']['code'],
                my_time)
            content += '現價: %s / 開盤: %s\n'%(
                stock_rt['realtime']['latest_trade_price'],
                stock_rt['realtime']['open'])
            content += '最高: %s / 最低: %s\n' %(
                stock_rt['realtime']['high'],
                stock_rt['realtime']['low'])
            content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])

            stock = twstock.Stock(text) #twstock.Stock('2330')
            content += '----\n'
            content += '最近五日價格: \n'
            price5 = stock.price[-5:][::-1]
            date5 = stock.date[-5:][::-1]
            for i in range(len(price5)):
                #content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d %H:%M:%S"), price5[i])
                content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=content)
            )
############################ 匯率區 ############################
    # if re.match('幣別種類', emsg):
    #     #message = show_Button()
    #     #line_bot_api.reply_message(event.reply_token, message)

    # #if re.match('[A-Z]{3}', msg):  #if re.match('查詢匯率[A-Z]{3}', msg):
    #     msg = msg[::]               #msg = msg[4:]
    #     content = showCurrency(msg)
    #     line_bot_api.push_message(uid, TextSendMessage(content))

    # if re.match("換匯[A-Z]{3}/[A-Z{3}]",msg):
    #     line_bot_api.push_message(uid,TextSendMessage("將為您做外匯計算...."))
    #     content = getExchangeRate(msg)
    #     line_bot_api.push_message(uid, TextSendMessage(content))

############################ 股價提醒 ############################
    if re.match("股價提醒", msg):
            line_bot_api.push_message(uid, TextSendMessage("請稍等..."))
            import schedule
            import time
            #查看當前股價
            def look_stock_price(stock, condition, price, userID):
                print(userID)
                url = "https://tw.stock.yahoo.com/q/q?s=" + stock
                list_req = requests.get(url)
                soup = BeautifulSoup(list_req.content, "html.parser")
                getstock = soup.findAll('span')[11].text
                content = stock + "當前股市價格為:" + getstock
                if condition == '<':
                    content += "\n篩選條件為: <" + price
                    if float(getstock) < float(price):
                        content += "\n符合" + getstock + "<" + price + "的篩選條件"
                        line_bot_api.push_message(userID, TextSendMessage(text = content))
                elif condition == '>':
                    content += "\n篩選條件為: >" + price
                    if float(getstock) > float(price):
                        content += "\n符合" + getstock + ">" + price + "的篩選條件"
                        line_bot_api.push_message(userID, TextSendMessage(text = content))
                elif condition == '<':
                    content += "\n篩選條件為: =" + price
                    if float(getstock) == float(price):
                        content += "\n符合" + getstock + "=" + price + "的篩選條件"
                        line_bot_api.push_message(userID, TextSendMessage(text = content))
            def job():
                print('HH')
                line_bot_api.push_message(uid, TextSendMessage("問就是直接ALL IN"))
                dataList = cache_users_stock()
                for i in range(len(dataList)):
                    for k in range(len(dataList[i])):
                        look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
            schedule.every(5).seconds.do(job).tag('daily-tasks-stock' + uid, "second")
        
            while True:
                schedule.run_pending()
                time.sleep(1)

############################ 粉絲/封鎖 訊息狀態 ############################

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """Hello! 您好，歡迎加入 熊安心 !

我是您最安心的小幫手 阿熊

任何機車相關資訊都可以在這裡找到
點選下方【選單】開始安心上路

加入熊安心～騎車更安心"""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(event.reply_token, message) #回覆你輸入的訊息(重複你說的話)

if __name__ =="__main__":
    app.run()



