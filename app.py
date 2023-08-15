#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.news import *
from events.Msg_Template import *
from events.map import *
from events.number import *
from model.mongodb import *
import re
import twstock
import datetime
from bs4 import BeautifulSoup
from events.MapQuickReply import *

app = Flask(__name__)


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



#——————————————————————————————————————————————附近位置———————————————————————————————————————————————————————————————————————————————————————————————————————————————————
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    # 使用者已分享位置
    latitude = event.message.latitude
    longitude = event.message.longitude
    user_location = f"{latitude},{longitude}" #使用者經緯度

    if user_location:
        buttons_template = ButtonsTemplate(
            title='您想查詢什麼？',
            text='請選擇以下的選項',
            actions=[
                PostbackAction(label='附近停車場', data=f"query={user_location}&type=parking"),
                PostbackAction(label='附近機車行', data=f"query={user_location}&type=motorcycle_repair"),
                PostbackAction(label='附近加油站', data=f"query={user_location}&type=gas_station")
            ]
        )
        template_message = TemplateSendMessage(
            alt_text='查詢選項',
            template=buttons_template
        )
        line_bot_api.reply_message(event.reply_token, template_message)
    else:
        reply_text = '無法獲取您的地理位置。'
        line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))

# Handle postback event when user selects an option
@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"
    data = event.postback.data
    queries = dict(q.split("=") for q in data.split("&"))

    location = queries.get('query', '')
    place_type = queries.get('type', '')

    if location and place_type:
        radius = 1000
        nearby_places = search_nearby_places(location, radius, place_type, api_key)
        places_names_chinese = {'parking': '停車場', 'motorcycle_repair': '機車行', 'gas_station': '加油站'}
        reply_text = f"附近的{places_names_chinese[place_type]}有：\n"

        for place in nearby_places:
            name = place['name']
            address = place.get('vicinity', '地址不詳')
            reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
        if not nearby_places:
            reply_text = f'附近沒有找到{places_names_chinese[place_type]}。'

        line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))


    # if user_location:
    #         radius = 1000
    #         nearby_parking = search_nearby_parking(user_location, radius, api_key)
    
    #         if nearby_parking:
    #             reply_text = '附近的停車場有：\n'
    #             for parking in nearby_parking:
    #                 name = parking['name']
    #                 address = parking.get('vicinity', '地址不詳')
    #                 #address = parking['vicinity']
    #                 reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
    #         else:
    #             reply_text = '附近沒有找到停車場。'
    # else:
    #     reply_text = '無法獲取您的地理位置。'

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextMessage(text=reply_text)
    # )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip() #使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱G

#————————————————————————————————————————————圖文選單———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
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
    
    
#————————————————————————————————————————————機車QuickReply———————————————————————————————————————————————————————————————————————————————————————————————————————————
    if re.match("我想看機車", msg):
        btn_msg = stock_reply_other()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    if re.match("附近支援", msg):
        btn_msg = MapAuickReply()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    

#————————————————————————————————————————————機車ptt討論版———————————————————————————————————————————————————————————————————————————————————————————————————————————

    if event.message.text == "大家最近都在討論什麼呢?":
        content_list = get_motor_ptt()  # 獲取前五筆資料的列表
        reply_content = '\n'.join(content_list)  # 將列表內容合併為文字訊息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_content))  # 使用TextSendMessage回覆訊息


############################ 粉絲/封鎖 訊息狀態 ############################

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """--MOTO熊 機車資訊站--
我是您的小幫手 🐻熊哥

【機車】資訊都可以在這裡找到
點選下方【選單】選擇更多服務

-加入motor熊 機車資訊不漏接-"""

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



