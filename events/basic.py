from line_bot_api import *

def about_us_event(event):

    emoji = [
            {
                "index":0,
                "productId":"5ac2213e040ab15980c9b447",
                "emojiID":"035"
            },
            {
                "index":11,
                "productId":"5ac2213e040ab15980c9b4475",
                "emojiID":"035"
            },
            {
                "index":23,
                "productId":"5ac1bfd5040ab15980c9b435",
                "emojiID":"091"

            },
            {
                "index":26,
                "productId":"5ac22c9e031a6752fb806d68",
                "emojiID":"042"

            }
        ]
    text_message = TextSendMessage(text='''$ 歡迎加入 熊安心 $
我是您最安心的小幫手 $ 熊哥

$ 機車 相關資訊都可以在這裡找到
點選下方【選單】開始安心上路

---加入熊安心 騎車更安心---''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='6632',
        sticker_id='11825396'
    )

    buttons_template = TemplateSendMessage(
        alt_text='小幫手 熊哥',
        template=ButtonsTemplate(
            title = '請選擇服務',
            text = '請選擇',
            thumbnail_image_url='https://i.imgur.com/GIVVWxG.jpg',
            actions = [
                MessageTemplateAction(
                    label = '油價查詢',
                    text = '油價查詢'
                ),
                MessageTemplateAction(
                    label = '匯率查詢',
                    text = '匯率查詢'
                ),
                MessageTemplateAction(
                    label='股價查詢',
                    text='股價查詢'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, buttons_template])
    