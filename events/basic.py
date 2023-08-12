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
                "productId":"5ac2213e040ab15980c9b447",
                "emojiID":"035"
            }
        ]
    text_message = TextSendMessage(text='''$ 歡迎加入 熊安心 $
我是您最安心的小幫手 🐻熊哥

【機車】相關資訊都可以在這裡找到
點選下方【選單】開始安心上路

---加入熊安心 騎車更安心---''', emojis=emoji)
    
    sticker_message = StickerSendMessage(
        package_id='6632',
        sticker_id='11825396'
    )
    
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message])

# -------------------------------
#     buttons_template = TemplateSendMessage(
# {
#   "type": "bubble",
#   "hero": {
#     "type": "image",
#     "url": "https://i.imgur.com/DfAoQGi.png",
#     "size": "full",
#     "aspectRatio": "20:13",
#     "aspectMode": "cover"
#   },
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "text",
#         "text": "我 是 小 幫 手 🐻 熊 哥",
#         "weight": "bold",
#         "size": "xl",
#         "align": "center"
#       },
#       {
#         "type": "box",
#         "layout": "baseline",
#         "margin": "md",
#         "contents": [
#           {
#             "type": "text",
#             "text": "👇 請 選 擇 服 務 項 目 👇",
#             "size": "lg",
#             "color": "#999999",
#             "align": "center"
#           }
#         ]
#       }
#     ]
#   },
#   "footer": {
#     "type": "box",
#     "layout": "vertical",
#     "spacing": "sm",
#     "contents": [
#       {
#         "type": "button",
#         "style": "primary",
#         "action": {
#           "type": "uri",
#           "label": "📰  最 新 資 訊",
#           "uri": "https://168.motc.gov.tw/theme/news"
#         },
#         "color": "#5B9A8B"
#       },
#       {
#         "type": "button",
#         "style": "primary",
#         "action": {
#           "type": "uri",
#           "label": "👍 熊 安 心 粉 絲 團",
#           "uri": "https://linecorp.com"
#         },
#         "color": "#5B9A8B"
#       },
#       {
#         "type": "button",
#         "action": {
#           "type": "uri",
#           "label": "🏍 我 想 看 機 車",
#           "uri": "https://autos.yahoo.com.tw/popular-bikes/"
#         },
#         "style": "primary",
#         "color": "#5B9A8B"
#       },
#       {
#         "type": "button",
#         "action": {
#           "type": "uri",
#           "label": "💬 網 友 最 新 話 題",
#           "uri": "https://www.ptt.cc/bbs/biker/index.html"
#         },
#         "style": "primary",
#         "color": "#5B9A8B"
#       },
#       {
#         "type": "button",
#         "action": {
#           "type": "postback",
#           "label": "📍 附 近 相 關 支 援",
#           "data": "hello"
#         },
#         "style": "primary",
#         "color": "#5B9A8B"
#       }
#     ],
#     "flex": 0
#   }
# }
#     )
#     line_bot_api.reply_message(
#         event.reply_token,
#         [text_message, sticker_message, buttons_template])
    

def show_Button():
    flex_message = FlexSendMessage(
            alt_text="熊哥幫幫我",
            contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/DfAoQGi.png",
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
          "type": "uri",
          "label": "📰  最 新 資 訊",
          "uri": "https://168.motc.gov.tw/theme/news"
        },
        "color": "#5B9A8B"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "uri",
          "label": "👍 熊 安 心 粉 絲 團",
          "uri": "https://linecorp.com"
        },
        "color": "#5B9A8B"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "🏍 我 想 看 機 車",
          "uri": "https://autos.yahoo.com.tw/popular-bikes/"
        },
        "style": "primary",
        "color": "#5B9A8B"
      },
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "💬 網 友 最 新 話 題",
          "uri": "https://www.ptt.cc/bbs/biker/index.html"
        },
        "style": "primary",
        "color": "#5B9A8B"
      },
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "📍 附 近 相 關 支 援",
          "data": "hello"
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