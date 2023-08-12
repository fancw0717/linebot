from line_bot_api import *

def stock_reply_other(stockNumber): #stockNumber
    content_text = "請選擇你要看的車種"
    text_message = TextSendMessage(
        text = content_text,
        quick_reply = QuickReply(
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
                            text = "跑車" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="街車",
                            text = "街車" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="美式機車",
                            text = "美式機車" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="越野車",
                            text = "越野車" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="休旅車",
                            text = "休旅車" 
                        )
                )
            ]
        ))
    return text_message

def show_sk1_Button():
    flex_message = FlexSendMessage(
        alt_text="速克達",
        contents={
            "type": "carousel",
            "contents": [
                {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://autos.yahoo.com.tw/p/r/w644/bike-models/May2023/DfE3hPr967G58vDt5VuK.png",
                        "size": "3xl"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "SYM Jet",
                                "size": "xl",
                                "align": "center"
                            }
                        ],
                        "alignItems": "center"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "👉 點 我 賞 車",
                                    "uri": "https://autos.yahoo.com.tw/new-bikes/model/sym-jet-sl-2023"
                                },
                                "style": "primary",
                                "color": "#005AB5"
                            }
                        ]
                    },
                    "size": "deca",
                    "styles": {
                        "header": {
                            "separatorColor": "#00CACA",
                            "backgroundColor": "#00CACA"
                        }
                    }
                },
                # 在這裡添加其他卡片的資訊，每個卡片類似上面的格式
            ]
        }
    )
    return flex_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "💵  幣  別  種  類  💵",
        "weight": "bold",
        "size": "xl",
        "color": "#AA2B1D",
        "margin": "none",
        "style": "italic"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "美金",
              "text": "USD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "日圓",
              "text": "JPY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "港幣",
              "text": "HKD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "英鎊",
              "text": "GBP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "澳幣",
              "text": "AUD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "加幣",
              "text": "CAD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "法郎",
              "text": "CHF"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新加坡",
              "text": "SGD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "南非幣",
              "text": "ZAR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞典幣",
              "text": "SEK"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "泰幣",
              "text": "THB"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "菲比索",
              "text": "PHP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "印尼幣",
              "text": "IDR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "韓元",
              "text": "KRW"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "馬來幣",
              "text": "MYR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009393",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "越南盾",
              "text": "VND"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "人民幣",
              "text": "CNY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "紐元",
              "text": "NZD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#01B468",
            "margin": "sm"
          }
        ]
      }
    ],
    "backgroundColor": "#ACD6FF",
    "borderWidth": "semi-bold",
    "spacing": "md",
    "margin": "xs",
    "offsetTop": "sm",
    "offsetBottom": "none",
    "offsetStart": "none",
    "offsetEnd": "none",
    "paddingAll": "sm",
    "paddingTop": "md",
    "paddingBottom": "lg",
    "paddingEnd": "lg",
    "paddingStart": "sm",
    "borderColor": "#ACD6FF"
  }
}
                    
    )
    return flex_message