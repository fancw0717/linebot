#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.news import *
from events.Msg_Template import *
from events.map import *
from events.number import *
from events.official import *
import requests
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
            title='請問您想查詢附近的哪個地方呢？',
            text='請選擇以下的選項',
            actions=[
                # 注意！！！需使用GOOGLE地圖上的地點類型 https://developers.google.com/maps/documentation/places/web-service/supported_types?hl=zh-tw
                # 選單不得超過四個
                PostbackAction(label='🅿️停車場', data=f"query={user_location}&type=parking"),
                PostbackAction(label='⛽加油站', data=f"query={user_location}&type=gas_station"),
                PostbackAction(label='🍽️附近餐廳', data=f"query={user_location}&type=restaurant"),
                PostbackAction(label='🛵機車行', data=f"query={user_location}&keyword=機車行")
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
def handle_postback(event):
    user_id = event.source.user_id
    api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"
    data = event.postback.data
    queries = dict(q.split("=") for q in data.split("&"))

    location = queries.get('query', '')
    place_type = queries.get('type', '')
    keyword = queries.get('keyword', '')

    radius = 1000  # This is your radius which you can adjust as needed.
    rank_by_distance = True  # Set this to True if you want results ranked by distance, else set to False

    if location and (place_type or keyword):
        nearby_places = search_nearby_places(location, radius, place_type, api_key, keyword, rank_by_distance)

        places_names_chinese = {'parking': '停車場',
                                'gas_station': '加油站',
                                'restaurant':'餐廳',
                                '機車行':'機車行'}
        place_description = places_names_chinese.get(place_type) or places_names_chinese.get(keyword)

        if nearby_places:
            carousel_columns = []
            for place in nearby_places[:10]:  # Limit to 10 due to carousel limitations
                name = place['name']
                address = place['vicinity']
                # Construct Google Maps navigation URL
                place_location = place['geometry']['location']
                nav_url = f"https://www.google.com/maps/dir/?api=1&destination={place_location['lat']},{place_location['lng']}"
                
                static_map_url = generate_static_map_url(place_location['lat'], place_location['lng'], api_key)

                column = CarouselColumn(
                    thumbnail_image_url=static_map_url,  # Display static map image
                    text=f'⭐{name[:25]}\n📌{address[:30]}',  # Ensure the text does not exceed 60 characters
                    actions=[
                        URIAction(label='導航', uri=nav_url)
                    ]
                )
                carousel_columns.append(column)

            carousel_template = CarouselTemplate(columns=carousel_columns)
            template_message = TemplateSendMessage(alt_text=f'附近的{place_description}', template=carousel_template)
            line_bot_api.reply_message(event.reply_token, template_message)
        else:
            reply_text = f'附近沒有找到{place_description}。'
            line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))
# @handler.add(PostbackEvent)
# def handle_postback(event):
#     user_id = event.source.user_id
#     api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"
#     data = event.postback.data
#     queries = dict(q.split("=") for q in data.split("&"))

#     location = queries.get('query', '')
#     place_type = queries.get('type', '')
#     keyword = queries.get('keyword', '')


#     if location and (place_type or keyword):
#         radius = 1000 # This is your radius which you can adjust as needed.
#         rank_by_distance = True  # Set this to True if you want results ranked by distance, else set to False
#         places_names_chinese = {'parking': '停車場',
#                                  'gas_station': '加油站',
#                                  'restaurant':'餐廳',
#                                  '機車行':'機車行'}
#         place_description = places_names_chinese.get(place_type) or places_names_chinese.get(keyword)
#         nearby_places = search_nearby_places(location, radius, place_type, api_key, keyword)

        
#         if nearby_places:
#             carousel_columns = []
#             for place in nearby_places[:10]:  # Limit to 10 due to carousel limitations
#                 name = place['name']
#                 address = place['vicinity']
#                 # Construct Google Maps navigation URL
#                 place_location = place['geometry']['location']
#                 nav_url = f"https://www.google.com/maps/dir/?api=1&destination={place_location['lat']},{place_location['lng']}"
                
#                 static_map_url = generate_static_map_url(place_location['lat'], place_location['lng'], api_key)

#                 column = CarouselColumn(
#                     thumbnail_image_url=static_map_url, # 加入這一行來顯示靜態地圖圖片
#                     text=f'⭐{name[:25]}\n📌{address[:30]}', # 確保文字不超過60個字符
#                     actions=[
#                         URIAction(label='導航', uri=nav_url)
#                     ]
#                 )
#                 carousel_columns.append(column)

            
#             carousel_template = CarouselTemplate(columns=carousel_columns)
#             template_message = TemplateSendMessage(alt_text=f'附近的{place_description}', template=carousel_template)
#             line_bot_api.reply_message(event.reply_token, template_message)
#         else:
#             reply_text = f'附近沒有找到{place_description}。'
#             line_bot_api.reply_message(event.reply_token, TextMessage(text=reply_text))

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



