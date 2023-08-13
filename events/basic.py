from line_bot_api import *

def about_us_event(event):

    emoji = [
            {
                "index":0,
                "productId":"5ac2213e040ab15980c9b447",
                "emojiID":"035"
            },
            {
                "index":14,
                "productId":"5ac2213e040ab15980c9b447",
                "emojiID":"035"
            }
        ]
    text_message = TextSendMessage(text='''$ MOTO熊 機車資訊站 $
我是您的小幫手 🐻熊哥

【機車】資訊都可以在這裡找到
點選下方【選單】選擇更多服務

-加入motor熊 機車資訊不漏接-''', emojis=emoji,)
    
    sticker_message = StickerSendMessage(
        package_id='11537',
        sticker_id='52002734'
    )
    

    aboutMethodMessage = aboutMethodButton()
    
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, aboutMethodMessage])

def aboutMethodButton():
    flex_message = FlexSendMessage(
        alt_text="我是小幫手熊哥",
        contents={
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://i.imgur.com/OIFNBzD.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "我 是 小 幫 手 🐻 熊 哥",
              "weight": "bold",
              "size": "xl",
              "align": "center"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "md",
              "contents": [
                {
                  "type": "text",
                  "text": "👇 請 選 擇 服 務 項 目 👇",
                  "size": "lg",
                  "color": "#999999",
                  "align": "center"
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "style": "primary",
              "action": {
                "type": "message",
                "label": "📰  最 新 消 息",
                "text": "最新消息"
              },
              "color": "#5B9A8B"
            },
            {
              "type": "button",
              "style": "primary",
              "action": {
                "type": "message",
                "label": "👍 各 品 牌 機 車 官 網 ",
                "text": "各品牌機車官網 "
              },
              "color": "#5B9A8B"
            },
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "🏍 我 想 看 機 車",
                "text": "我想看機車"
              },
              "style": "primary",
              "color": "#5B9A8B"
            },
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "💬 網 友 最 新 話 題",
                "text": "網友都在聊什麼"
              },
              "style": "primary",
              "color": "#5B9A8B"
            },
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "📍 附 近 相 關 支 援",
                "text": "附近相關支援"
              },
              "style": "primary",
              "color": "#5B9A8B"
            }
          ],
          "flex": 0
        }
      }
    )
    return flex_message
