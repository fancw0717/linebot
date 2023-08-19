from line_bot_api import *
import requests
import flask
  
#———————————————————————————————————————————QuickReply———————————————————————————————————————————
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
                )
            ]
        ))
    return text_message



#————————————————————————————————————————— 首先是生成 Google Maps 靜態圖片 URL 的函數—————————————————————————————————————————————————————————
def generate_static_map_url(latitude, longitude, api_key):
    base_url = "https://maps.googleapis.com/maps/api/staticmap"
    parameters = {
        "center": f"{latitude},{longitude}",
        "zoom": 16,
        "size": "600x300",
        "maptype": "roadmap",
        "markers": f"color:red%7Clabel:P%7C{latitude},{longitude}",
        "key": api_key
    }

    return base_url + "?" + "&".join(f"{k}={v}" for k, v in parameters.items())

#——————————————————————————————————————————— map相關參數 —————————————————————————————————————————————————————————

# def search_nearby_places(location, radius, place_type=None, api_key="", keyword=None):
#     base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
#     params = {
#         "location": location,
#         "radius": radius,
#         "key": api_key
#     }
    
#     if place_type:
#         params["type"] = place_type
#     if keyword:
#         params["keyword"] = keyword

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     if data['status'] == 'OK':
#         return data['results']
#     else:
#         print(f"搜尋附近的地點失敗。狀態:", data['status'])
#         return []

def search_nearby_places(location, radius=1000, place_type=None, api_key="", keyword=None, rank_by_distance=False):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "key": api_key
    }
    
    if rank_by_distance:
        params["rankby"] = "distance"
    else:
        params["radius"] = radius
    
    if place_type:
        params["type"] = place_type
    if keyword:
        params["keyword"] = keyword

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        return data['results']
    else:
        print(f"搜尋附近的地點失敗。狀態:", data['status'])
        return []