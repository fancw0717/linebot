from line_bot_api import *

def Official_Website():
    content_text = "官方網站"
    text_message = TextSendMessage(
        text = content_text,
        quick_reply = QuickReply(
            items=[
                QuickReplyButton(
                        action = MessageAction(
                            label="YAHAMA",
                            text = "https://www.yamaha-motor.com.tw/index.aspx",
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="KMYCO",
                            text = "https://www.kymco.com.tw/" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="SYM",
                            text = "https://tw.sym-global.com/mmbcu?utm_source=GoogleAdWords&utm_campaign=MMB&utm_medium=sem" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="PGO",
                            text = "https://pgo.com.tw/index/" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="SUZUKI",
                            text = "https://www.suzukimotor.com.tw/" 
                        )
                ),
                QuickReplyButton(
                        action = MessageAction(
                            label="GOGORO",
                            text = "https://www.gogoro.com/tw/" 
                        )
                )
            ]
        ))
    return text_message