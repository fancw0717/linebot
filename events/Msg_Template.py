from line_bot_api import *

def stock_reply_other():
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

def show_bk1_Button():
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
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/January2023/pFUsL0xCiz9UetyFNxGf.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "SYM 迪爵Duke",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/sym-%E8%BF%AA%E7%88%B5duke-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/April2023/XeHcJwfD55MOTMxVFjWx.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Kymco GP",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/kymco-gp-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/June2023/Tiv2HnckKQGVEbCb5yvf.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "SYM CLBCU",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/sym-clbcu-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/April2023/zrOl106LVIBMmp0Dyi79.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "SYM DRG",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/sym-drg-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}
    )
    return flex_message
############################# 跑車輪播 #############################
def show_bk2_Button():
    flex_message = FlexSendMessage(
        alt_text="跑車",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/2pBDh1sDX3e86UEjZekY.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda CBR650",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-cbr650-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/g2G1TLrCD6El1AwIT5NX.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Kawasaki Ninja",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/kawasaki-ninja-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/March2023/ZejxoQX1Dy3yGQjkOxP7.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "BMW S Series",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/bmw-s-series-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/January2023/sSToVaBMxGbYCyhPq1oT.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Yamaha YZF-R",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/yamaha-yzf-r-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/January2023/RDDhaesT6lJeipSdLTlq.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda CBR500",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-cbr500-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}

      )
    return flex_message

############################# 街車輪播 #############################
def show_bk3_Button():
    flex_message = FlexSendMessage(
        alt_text="街車",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/mByqjz3urlsbWaK8OtcE.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Kawasaki Z",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/kawasaki-z-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/cNnbIKpWQvekNKpH9BmB.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda CB650",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-cb650-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/TzhhAxInlcWS208GslNj.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda MSX",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-msx-grom-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/April2023/j8Eddet7J6HuQXLT4SIb.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "SYM 野狼",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/sym-%E9%87%8E%E7%8B%BC-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/September2022/CnTyqRCsQdqLI82xSInD.jpeg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda CB300",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-cb300-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}

      )
    return flex_message

############################# 美式機車輪播 #############################
def show_bk4_Button():
    flex_message = FlexSendMessage(
        alt_text="美式機車",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/vrVlNHjboou5P77nYA4O.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda Rebel",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-rebel-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/oCFZuuNZFuapcQ7DodYi.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Harley-Davidson Softail",
            "size": "md",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/harley-davidson-softail-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/June2023/kmqd6ysGKzqEIdWb6MxC.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Kawasaki Vulcan",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/kawasaki-vulcan-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/hn11huWJ3olyxohvTdts.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Harley-Davidson Sportster",
            "size": "sm",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/harley-davidson-sportster-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/o4PzffqmcO1QtzC2bimt.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Triumph Rocket",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/triumph-rocket-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}

      )
    return flex_message

############################# 越野車輪播 #############################
def show_bk5_Button():
    flex_message = FlexSendMessage(
        alt_text="越野車",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/April2023/PdzfzGSr2aLSbEl8pF5H.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda CRF300",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-crf300-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/November2022/zpfFs2roKMFRbWrUQrmX.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda Africa Twin",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-africa-twin-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/January2023/XWDdquM4qrVsR12vvS8c.png",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Yamaha Tenere",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/yamaha-tenere-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/3vi81bCEm0AncKcoSIrc.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Husqvarna FE",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/husqvarna-fe-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/April2023/RPgKv94uQhDFfFTh70YP.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Ducati Desert X",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/ducati-desert-x-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}

      )
    return flex_message
############################# 休旅車輪播 #############################
def show_bk6_Button():
    flex_message = FlexSendMessage(
        alt_text="休旅車",
        contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/77hagow1qppMs80EddxL.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Suzuki V-Strom",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/suzuki-v-strom-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/March2023/NyzaDusxs1hjrFMRm68O.jpeg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda Goldwing",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-goldwing-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/22vTIjAttgjDbDW800Sb.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "BMW R Series",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/bmw-r-series-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/May2023/nxOecNzGjgrmxM36PFjz.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Triumph Tiger",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/triumph-tiger-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    },
    {
      "type": "bubble",
      "size": "deca",
      "hero": {
        "type": "image",
        "url": "https://autos.yahoo.com.tw/p/r/w880/bike-models/September2022/zjpd7H9fFoMrBgAHvszD.jpg",
        "size": "3xl"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Honda X-ADV",
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
              "uri": "https://autos.yahoo.com.tw/new-bikes/model/honda-x-adv-2023"
            },
            "style": "primary",
            "color": "#005AB5"
          }
        ]
      },
      "styles": {
        "header": {
          "separatorColor": "#00CACA",
          "backgroundColor": "#00CACA"
        }
      }
    }
  ]
}

      )
    return flex_message