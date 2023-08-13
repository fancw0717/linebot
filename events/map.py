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

#def handle_message(event):


# # 在這裡替換為你設定的 Webhook URL
# webhook_url = "YOUR_WEBHOOK_URL"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80)