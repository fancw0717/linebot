from line_bot_api import *
from events.basic import *
from events.oil import *
from events.Msg_Template import *
from events.EXRate import *
from events.map import *
from model.mongodb import*
import re
import twstock
import datetime
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
#---------------------------監聽
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        
    return 'OK'
#----------------------------處理
@handler.add(MessageEvent, message=TextMessage)
@handler.add(MessageEvent, message=LocationMessage)
def get_user_location(user_id, api_key):
    base_url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.post(base_url, json={})
    data = response.json()

    if "location" in data:
        location_lat = data['location']['lat']
        location_lng = data['location']['lng']
        print(f"使用者 {user_id} 的地點：緯度 {location_lat}, 經度 {location_lng}")
        return f"{location_lat},{location_lng}"

    else:
        print("無法獲取使用者地點。")
        return None

def search_nearby_parking(location, radius, api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": "parking",
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        return data['results']
    else:
        print("搜尋附近停車場失敗。狀態:", data['status'])
        return []


def handle_text_message(event):
    if event.message.text == '我要分享位置':
        # 讓使用者分享位置
        reply_message = '請點選下方的「位置」按鈕，然後選擇「傳送位置」。'
    else:
        # 其他處理邏輯
        reply_message = '請點擊下方按鈕來分享位置。'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=reply_message)
    )

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):

    
    user_id = event.source.user_id
    api_key = "AIzaSyBuh_ZmBbKBjvtG95pGzaW2-bf77Vc2QoY"

# 使用者已分享位置
    latitude = event.message.latitude
    longitude = event.message.longitude

# 進一步處理取得的位置資訊，例如使用 Google Maps API 來查詢地理資訊
# ...

    reply_message = f'你的位置是：緯度 {latitude}，經度 {longitude}'
    
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
      
if __name__ == "__main__":
    app.run()


