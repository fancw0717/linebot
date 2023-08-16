#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#Channel access token #在line Developers的providers的Basic settings
line_bot_api = LineBotApi('aEqzPu8GT8eTBISPBK0ud6aLwnINJ+iZgW8Su9M+T626pCm77+6SE714q2HI3QkbdBQ+iWRs4rsNNNhOJhAP3Q1Q1JE1RUuV+0JVB9pw5riZ5AIJ57uNeJnSwvubHiTQqE9v6Td1j4fBdvQ0FOGcUQdB04t89/1O/w1cDnyilFU=')
#Channel secret  #在line Developers的providers的Messaging API
handler = WebhookHandler('476740fd390b4f6d726e46b055c207df')