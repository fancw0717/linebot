#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.map import *
from events.ptt import *
import re
import datetime
from bs4 import BeautifulSoup

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

#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    message_text = str(event.message.text).lower()
    msg = str(event.message.text).upper().strip() #使用者輸入的內容
    emsg = event.message.text
    user_name = profile.display_name #使用者名稱
   
############################ 使用說明 選單 我想看幾車 ############################
def handle_message(event):
    msg = event.message.text

    if '我想看幾車' in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='a quick reply message',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(
                                        label="速克達",
                                        text = "速克達",
                            )
                        ),
                        QuickReplyButton(
                            action = MessageAction(
                                        label="跑車",
                                        text = "跑車",
                            )
                        ),
                        # return a location message
                        QuickReplyButton(
                            action = MessageAction(
                                        label="街車",
                                        text = "街車",
                            )
                        ),
                        QuickReplyButton(
                            action = MessageAction(
                                        label="美式機車",
                                        text = "美式機車",
                            )
                        ),
                        QuickReplyButton(
                            action = MessageAction(
                                        label="越野車",
                                        text = "越野車",
                            )
                        ),
                        QuickReplyButton(
                            action = MessageAction(
                                        label="休旅車",
                                        text = "休旅車",
                            )
                        )
                    ])))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )


# Handle PostbackEvent
@handler.add(PostbackEvent)
def handle_message(event):
    data = event.postback.data
    if data == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))

    
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


if __name__ =="__main__":
    app.run()



