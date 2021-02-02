# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import requests

class ActionGetWeather(Action):
    """ Return today's weather forecast"""

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):

        city = tracker.get_slot('location')
        api_token = "417d2d3d5443b9068b0580a5e3414961"
        url = "https://api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": api_token, "units": "metric", "lang": "vi"}
        response = requests.get(url, params=payload)
        if response.ok:
            description = response.json()["weather"][0]["description"]
            temp = round(response.json()["main"]["temp"])
            cityGR = response.json()["name"]

            msg = f"Nhiệt độ tại {city} hiện tại là {temp} độ C và {description}"
        else:
            msg= "Lỗi!"

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]
class ActionGetWeatherForecasts(Action):
    """ Return today's weather forecast"""

    def name(self):
        return "action_get_weather_forecasts"

    def run(self, dispatcher, tracker, domain):

        city = 'Ho Chi Minh'
        api_token = "417d2d3d5443b9068b0580a5e3414961"
        url = "https://api.openweathermap.org/data/2.5/onecall?"
        payload = {"lat": "10.75", "lon" : "106.6667","appid": api_token, "exclude":"hourly,daily.dt",  "units": "metric", "lang": "vi"}
        response = requests.get(url, params=payload)
        if response.ok:
            # temp = round(response.json()["main"]["temp"])
            # cityGR = response.json()["name"]
            daily = response.json()["daily"][2]
            temp = daily["temp"]["day"]
            description = daily["weather"][0]["description"]

            msg = f"Nhiệt độ tại {city} vào ngày mai là {temp} độ C và {description}"
        else:
            msg= "Lỗi!"

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]    

class ActionMessengerTemplate(Action):
    def name(self):
        return "action_api"
    async def run(self, dispatcher, tracker, domain):
        def Star(star):

            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
                # ⭐
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        response = requests.get("http://[::1]:3001/place-travels")
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            type = value["type"]
            image = value["image"]
            review = value["review"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {}\nReview: {}\nĐánh giá: {} {}".format(type, review,star, Star(star)),
                        "default_action": {
                            "type": "web_url",
                            "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                            "webview_height_ratio": "tall",
                        },
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                "title": "Chi tiết"
                            },
                            {
                                "type" : "web_url",
                                "url" : "https://www.google.com/maps/dir/Chung+Cư+Tôn+Thất+Đạm/Ben+Thanh+Market,+Đ.+Lê+Lợi,+Phường+Bến+Thành,+Quận+1,+Thành+phố+Hồ+Ch%C3%AD+Minh+700000,+Vietnam/@10.7696324,106.6992905,17z/am=t/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x31752f41a16fd0b1:0x3de467bc89abc2aa!2m2!1d106.7040672!2d10.7695854!1m5!1m1!1s0x31752f3f3129e64d:0x8d6b2d79522c7f30!2m2!1d106.6982784!2d10.7721095!3e0",
                                "title": "Chỉ đường"
                            }
                        ]
                    },
            else:
                _elements += {
                                "title": "{}. {}".format(index+1,name),
                                "image_url": "{}".format(image),
                                "subtitle": "Loại địa điểm: {}\nReview: {}\nĐánh giá: {} {}    ".format(type, review,star, Star(star)),
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                        "title": "Chi tiết"
                                    },
                                    {
                                        "type" : "web_url",
                                        "url" : "https://www.google.com/maps/dir/Chung+Cư+Tôn+Thất+Đạm/Ben+Thanh+Market,+Đ.+Lê+Lợi,+Phường+Bến+Thành,+Quận+1,+Thành+phố+Hồ+Ch%C3%AD+Minh+700000,+Vietnam/@10.7696324,106.6992905,17z/am=t/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x31752f41a16fd0b1:0x3de467bc89abc2aa!2m2!1d106.7040672!2d10.7695854!1m5!1m1!1s0x31752f3f3129e64d:0x8d6b2d79522c7f30!2m2!1d106.6982784!2d10.7721095!3e0",
                                        "title": "Chỉ đường"
                                    }
                                ]
                            },
        gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": _elements
                }
            }
        }
        dispatcher.utter_custom_json(gt)
        return []

    
class ActionTransport(Action):
    def name(self):
        return "action_transport"
    def run(self, dispatcher, tracker, domain):
        transport = {
            "text": "Có 3 loại phương tiện phổ biến:",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"Máy bay",
                "payload":"<POSTBACK_PAYLOAD>",
                # "image_url":"http://example.com/img/red.png"
            },{
                "content_type":"text",
                "title":"Tàu hoả",
                "payload":"<POSTBACK_PAYLOAD>",
                # "image_url":"http://example.com/img/green.png"
            },{
                "content_type":"text",
                "title":"Xe khách",
                "payload":"<POSTBACK_PAYLOAD>",
                # "image_url":"http://example.com/img/green.png"
            },
            ],
            "text": "Bạn muốn di chuyến bằng phương tiện nào ?"
            
        }
        dispatcher.utter_custom_json(transport)
        return []  

class ActionWebView(Action):
    def name(self):
        return "action_coordinates"
    def run(self, dispatcher, tracker, domain):
        transport = {
        
        }
        dispatcher.utter_custom_json(transport)
        return []  
    
class ActionFind(Action):
    def name(self):
        return "action_hotels"
    async def run(self, dispatcher, tracker, domain):
        filterStar = tracker.get_slot('star')
        if (filterStar == None or float(filterStar) > 5):
            filterStar = 5
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        URL = "http://localhost:3001/hotels?filter=%7B%0A%20%20%22where%22%3A%20%7B%0A%20%20%20%20%22star%22%3A%20%22{}%22%0A%20%20%7D%0A%7D".format(filterStar)
        # URL = "http://localhost:3001/hotels"
        # PARAM1 = '{"where": {"star": "3" }}'
        # PARAMS = { "filter": "{}".format(PARAM1)  }
        response = requests.get(url = URL)
        jsonResponse = response.json()
        # print(PARAM0)
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            # image = value["image"]
            image = "https://static.asiawebdirect.com/m/bangkok/portals/vietnam/homepage/ho-chi-minh-city/top10/top10-ho-chi-minh-hotels-romantic/pagePropertiesImage/10-best-hcmc-romantic-hotels.jpg"
            discount = value["discount"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Loại địa điểm: {}\nDiscount: {}\nĐánh giá: {} {}".format(price, discount,star, Star(star)),
                        "default_action": {
                            "type": "web_url",
                            "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                            "webview_height_ratio": "tall",
                        },
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                "title": "Chi tiết"
                            },
                            {
                                "type": "postback",
                                "title": "Chỉ đường",
                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                            }
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Loại địa điểm: {}\nDiscount: {}\nĐánh giá: {} {}".format(price, discount,star, Star(star)),
                               "default_action": {
                                   "type": "web_url",
                                   "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                   "webview_height_ratio": "tall",
                               },
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                       "title": "Chi tiết"
                                   },
                                   {
                                       "type": "postback",
                                       "title": "Chỉ đường",
                                       "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                   }
                               ]
                            },
        gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": _elements
                }
            }
        }
        dispatcher.utter_custom_json(gt)
        return []