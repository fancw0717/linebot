#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.news import *
from events.Msg_Template import *
from events.map import *
from events.number import *
from events.official import *
import re
import twstock
import datetime
from bs4 import BeautifulSoup


app = Flask(__name__)
#——————————————————————————————————————— 監聽所有來自callback的 Post Request ————————————————————————————————————————————————


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
                PostbackAction(label='附近加油站', data=f"query={user_location}&type=gas_station"),
                #PostbackAction(label='附近美食', data=f"query={user_location}&type=food")
                PostbackAction(label='附近摩托車店', data=f"query={user_location}&type=motorcycle_shop")
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


#——————————————————————————————————— Handle postback event when user selects an option —————————————————————————————————————————————————————————————————————

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"
    data = event.postback.data
    queries = dict(q.split("=") for q in data.split("&"))

    location = queries.get('query', '')
    place_type = queries.get('type', '')

    if location and place_type:
        radius = 1500
        nearby_places = search_nearby_places(location, radius, place_type, api_key)
        places_names_chinese = {'parking': '停車場', 'gas_station': '加油站','motorcycle_shop':'摩托車店'}
        if nearby_places:
            carousel_columns = []
            for place in nearby_places[:10]:  # Limit to 10 due to carousel limitations
                name = place['name']
                address = place.get('vicinity', '地址不詳')
                # Construct Google Maps navigation URL
                place_location = place['geometry']['location']
                nav_url = f"https://www.google.com/maps/dir/?api=1&destination={place_location['lat']},{place_location['lng']}"
                
                static_map_url = generate_static_map_url(place_location['lat'], place_location['lng'], api_key)
                print(static_map_url)

                column = CarouselColumn(
                    text=f'⭐名稱: {name}\n📌地址: {address}',
                    actions=[
                        URIAction(label='導航', uri=nav_url)
                    ]
                )
                carousel_columns.append(column)

            
            carousel_template = CarouselTemplate(columns=carousel_columns)
            template_message = TemplateSendMessage(
                alt_text=f'附近的{places_names_chinese[place_type]}',
                template=carousel_template
            )
            line_bot_api.reply_message(event.reply_token, template_message)
        else:
            reply_text = f'附近沒有找到{places_names_chinese[place_type]}。'
            line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))

#———————————————————————————————————————————— 文字監聽 ————————————————————————————————————————————————————————————————————————————————————————————————————————

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip() #使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱G


#———————————————————————————————————————————— 圖文選單 ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    
    if message_text == '熊哥幫幫我':
        about_us_event(event)
    
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
    
    
#———————————————————————————————————————————— 機車QuickReply ———————————————————————————————————————————————————————————————————————————————————————————————————————————
    if message_text == '最新消息':
        news_content = get_latest_news()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=news_content))

    if re.match("機車品牌官網", msg):
        btn_msg = Official_Website()
        line_bot_api.push_message(uid, btn_msg)
        return 0
   
    if re.match("我想看機車", msg):
        btn_msg = stock_reply_other()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
    if re.match("附近支援", msg):
        btn_msg = MapAuickReply()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    
#———————————————————————————————————————————— 機車ptt討論版 ———————————————————————————————————————————————————————————————————————————————————————————————————————————

    if event.message.text == "大家最近都在討論什麼呢?":
        content_list = get_motor_ptt()  # 獲取前五筆資料的列表
        reply_content = '\n'.join(content_list)  # 將列表內容合併為文字訊息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_content))  # 使用TextSendMessage回覆訊息

#———————————————————————————————————————————— 粉絲/封鎖 訊息狀態 ————————————————————————————————————————————

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



