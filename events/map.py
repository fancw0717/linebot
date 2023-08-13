from line_bot_api import *
import requests

def google_map(event):
    
    buttons_map = TemplateSendMessage(
            alt_text= '附近資訊',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                actions=[
                    MessageTemplateAction(
                        label='附近停車場',
                        text='附近停車場'
                    ),
                    MessageTemplateAction(
                        label='附近加油站',
                        text='附近加油站'
                    ),
                    MessageTemplateAction(
                        label='附近機車行',
                        text='附近機車行'
                    ),
                    MessageTemplateAction(
                        label='附近美食',
                        text='附近美食'
                    )
                ]
            )
        )
    line_bot_api.reply_message(
        event.reply_token, 
        [buttons_map]
    )


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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # 假設這是使用者的地理座標（25.0330,121.5654）
    user_location = "25.0330,121.5654"
    radius = 1000
    api_key = "AIzaSyD_L0ps7XVyXnBZQQnbXr4p2seh2XbvsD0"

    nearby_parking = search_nearby_parking(user_location, radius, api_key)
    
    if nearby_parking:
        reply_text = '附近的停車場有：\n'
        for parking in nearby_parking:
            name = parking['name']
            address = parking['vicinity']
            reply_text += f'名稱: {name}\n地址: {address}\n----------\n'
    else:
        reply_text = '附近沒有找到停車場。'

    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=reply_text)
    )

# 在這裡加入其他處理 MessageEvent 的程式碼...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)