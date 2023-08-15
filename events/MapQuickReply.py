from line_bot_api import *

def MapAuickReply():
    content_text = "附近支援"
    text_message = TextSendMessage(
        text = content_text,
        quick_reply = QuickReply(
            items=[
                QuickReplyButton(
                        action = LocationAction(
                            label="分享位置",
                            text = "分享位置",
                        )
                ),
            ]
        ))
    return text_message
