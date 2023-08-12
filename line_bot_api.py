#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import(LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

#Channel access token #在line Developers的providers的Basic settings
line_bot_api = LineBotApi('Fgm1PZljto93lSH0NGfZcisx1YapoloDzRIcm4yUpWRt1luWNX+Ap6A1IcFGGOHpFOKRhMJ5olMurHOH1ylvR3fkOKsxR29KxeURfRj0/vRlZoHdylq+Vt+DQPAyE6vU4pOtZIkh0YTnZniBPYxrKAdB04t89/1O/w1cDnyilFU=')
#Channel secret  #在line Developers的providers的Messaging API
handler = WebhookHandler('b4d0c49e7ac03e0fdcc331ab66600c0e')