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
import locale
import json
import requests
import re

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
        return "action_get_weather_forecasts_day"

    def run(self, dispatcher, tracker, domain):
        numForecast = int(tracker.get_slot('num_forecasts_day'))
        print(numForecast)
        image = "https://bloximages.newyork1.vip.townnews.com/northwestgeorgianews.com/content/tncms/assets/v3/editorial/9/6d/96da56b4-2286-11e3-aa4e-0019bb30f31a/565e129375c24.image.jpg"
        
        city = 'Ho Chi Minh'
        api_token = "417d2d3d5443b9068b0580a5e3414961"
        url = "https://api.openweathermap.org/data/2.5/onecall?"
        payload = {"lat": "10.75", "lon" : "106.6667","appid": api_token, "exclude":"hourly,daily.dt",  "units": "metric", "lang": "vi"}
        response = requests.get(url, params=payload)
        if response.ok:
            _elements = "",
            _tempsElements = "",
            name = "Nhiệt độ tại Hồ Chí Minh"
            for index in range(numForecast):  
                daily = response.json()["daily"][index]
                temp = daily["temp"]["day"]
                description = daily["weather"][0]["description"]
                if _elements == _tempsElements:
                    _elements = {
                            "title": "{}. {}".format(index+1, name),
                            "image_url": "{}".format(image),
                            "subtitle": "Nhiệt độ: {} độ C\nChi tiết: {}".format(temp, description),
                            "default_action": {
                                "type": "web_url",
                                "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                "webview_height_ratio": "tall",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": "https://weather.com/weather/today/l/10.82,106.63?par=google&temp=c",
                                    "title": "Chi tiết"
                                },
                            ]
                        },
                else:
                    daily = response.json()["daily"][index]
                    temp = daily["temp"]["day"]
                    description = daily["weather"][0]["description"]
                    _elements += {
                                    "title": "{}. {}".format(index+1, name),
                                    "image_url": "{}".format(image),
                                    "subtitle": "Nhiệt độ: {} độ C\nChi tiết: {}  ".format(temp, description),
                                    "default_action": {
                                        "type": "web_url",
                                        "url": "https://vi.wikipedia.org/wiki/Chợ_Bến_Thành",
                                        "webview_height_ratio": "tall",
                                    },
                                    "buttons": [
                                      {
                                    "type": "web_url",
                                    "url": "https://weather.com/weather/today/l/10.82,106.63?par=google&temp=c",
                                    "title": "Chi tiết"
                                },
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
        else:
           dispatcher.utter_message("Lỗi!")

        return []    
class ActionGetWeatherForecasts7Day(Action):
    """ Return today's weather forecast"""

    def name(self):
        return "action_get_weather_forecasts"

    def run(self, dispatcher, tracker, domain):
        image = "https://media-exp1.licdn.com/dms/image/C4E1BAQHFBSfHZ6Gdnw/company-background_10000/0/1531778159831?e=2159024400&v=beta&t=Z3tagxGq5I5UlFxzBxxcIqb90ipG3gzeSRAtv9y2d-Y"
        
        city = 'Ho Chi Minh'
        api_token = "417d2d3d5443b9068b0580a5e3414961"
        url = "https://api.openweathermap.org/data/2.5/onecall?"
        payload = {"lat": "10.75", "lon" : "106.6667","appid": api_token, "exclude":"hourly,daily.dt",  "units": "metric", "lang": "vi"}
        response = requests.get(url, params=payload)
        if response.ok:
            
            name = "Nhiệt độ tại Hồ Chí Minh"
            
            daily = response.json()["daily"][0]
            temp = daily["temp"]["day"]
            description = daily["weather"][0]["description"]
            
            _elements = {
                        "title": "{}. {}".format(1, name),
                        "image_url": "{}".format(image),
                        "subtitle": "Nhiệt độ: {} độ C\nChi tiết: {}".format(temp, description),
                        "buttons": [
                           {
                                    "type": "web_url",
                                    "url": "https://weather.com/weather/today/l/10.82,106.63?par=google&temp=c",
                                    "title": "Chi tiết"
                                },
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
        else:
           dispatcher.utter_message("Lỗi!")

        return [SlotSet("location", None)]    
class ActionPlaceTravel(Action):
    def name(self):
        return "action_placeTravel"
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
        response = requests.get("http://localhost:3001/place-travels")
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index in range(10):  
            name = jsonResponse[index]["name"]
            type = jsonResponse[index]["type"]
            image = jsonResponse[index]["image"]
            review = jsonResponse[index]["review"]
            star = jsonResponse[index]["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Loại địa điểm: {}\nReview: {}\nĐánh giá: {} {}".format(type, review,star, Star(star)),
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

class ActionPlaceTravelType(Action):
    def name(self):
        return "action_placeTravel_type"
    async def run(self, dispatcher, tracker, domain):
        PAGODA = ["cúng bái", "Chua cau duyen", "cau duyen","Chùa cầu con","Chua cau duyen","Cầu tài lộc" "chúc phúc", "cầu duyên", "ngôi chùa", "Chùa", "đi tu"]
        SHOPING = ["mua sắm","mua đồ", "shopping", "shoping", "mua", "sắm", "đồ", "quần áo", "clothes", "trung tâm thương mại"]
        BEAUTYSPOT = ["danh lam thắng cảnh", "đẹp", "danh lam", "thắng cảnh", "view đẹp"]
        CHURCH = ["nhà thờ", "đi lễ", "chúa"]
        ENTERTAINMENT = ["vui chơi", "giải trí", "công viên", "chơi"]
        typeTravel = tracker.get_slot('typeTravel')
        findType = "shopping"
        for i,value in enumerate(PAGODA):
            if typeTravel == value :
                findType = "pagoda"
                break
        for i,value in enumerate(SHOPING):
            if typeTravel == value :
                findType = "shopping"
                break
        for i,value in enumerate(BEAUTYSPOT):
            if typeTravel == value :
                findType = "beautySpot"
                break
        for i,value in enumerate(ENTERTAINMENT):
            if typeTravel == value :
                findType = "entertainment"
                break
        for i,value in enumerate(CHURCH):
            if typeTravel == value :
                findType = "church"
                break
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
        URL = "http://localhost:3001/place-travels?filter=%7B%0A%20%20%22where%22%3A%20%7B%0A%20%20%20%20%22type%22%3A%20%22{}%22%0A%20%20%7D%0A%7D".format(findType)
        response = requests.get(URL)
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
                        "subtitle": "Loại địa điểm: {}\nReview: {}\nĐánh giá: {} {}".format(type, review,star, Star(star)),
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
                "payload":"/plane",
                # "image_url":"http://example.com/img/red.png"
            },{
                "content_type":"text",
                "title":"Tàu hoả",
                "payload":"/train",
                # "image_url":"http://example.com/img/green.png"
            },{
                "content_type":"text",
                "title":"Xe khách",
                "payload":"/coach",
                # "image_url":"http://example.com/img/green.png"
            },
            ],
            "text": "Bạn muốn di chuyến bằng phương tiện nào ?"
            
        }
        dispatcher.utter_custom_json(transport)
        return []  
class ActionTransportInSG(Action):
    def name(self):
        return "action_transport_inSG"
    def run(self, dispatcher, tracker, domain):
        transport = {
            "text": "Có 3 loại phương tiện phổ biến:",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"Taxi",
                "payload":"/taxi",
                # "image_url":"http://example.com/img/red.png"
            },{
                "content_type":"text",
                "title":"Xe máy",
                "payload":"/motorcycle",
                # "image_url":"http://example.com/img/green.png"
            },{
                "content_type":"text",
                "title":"Xe bus",
                "payload":"/bus",
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
    
class ActionFindHotels(Action):
    def name(self):
        return "action_hotels"
    async def run(self, dispatcher, tracker, domain):
        # number = int(tracker.get_slot('number'))
        number = 10
            
        print(number)
        URL ="http://localhost:3001/hotels"
         
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        response = requests.get(url = URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index in range(10):  
            name = jsonResponse[index]["name"]
            price = jsonResponse[index]["price"]
            # image = jsonResponse[index]["image"]
            image = jsonResponse[index]["image"]
            discount = jsonResponse[index]["discount"]
            star = jsonResponse[index]["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
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
            elif index < number:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
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

class ActionFindDistrictHotels(Action):
    def name(self):
        return "action_hotels_find_district"
    async def run(self, dispatcher, tracker, domain):
        district = tracker.get_slot('district')
        Q1 = ["Quận 1", "Q1", "q1", "quận 1", "quận1", "Quận1", "1"]
        Q2 = ["Quận 2", "Q2", "q2", "quận 2", "quận2", "Quận2", "2"]
        Q3 = ["Quận 3", "Q3", "q3", "quận 3", "quận3", "Quận3", "3"]
        Q4 = ["Quận 4", "Q4", "q4", "quận 4", "quận4", "Quận4", "4"]
        Q5 = ["Quận 5", "Q5", "q5", "quận 5", "quận5", "Quận5", "5"]
        Q6 = ["Quận 6", "Q6", "q6", "quận 6", "quận6", "Quận6", "6"]
        Q7 = ["Quận 7", "Q7", "q7", "quận 7", "quận7", "Quận7", "7"]
        Q8 = ["Quận 8", "Q8", "q8", "quận 8", "quận8", "Quận8", "8"]
        Q9 = ["Quận 9", "Q9", "q9", "quận 9", "quận9", "Quận9", "9"]
        Q10 = ["Quận 10", "Q10", "q10", "quận 10", "quận10", "Quận10", "10"]
        Q11 = ["Quận 11", "Q11", "q11", "quận 11", "quận11", "Quận11", "11"]
        Q12 = ["Quận 12", "Q12", "q12", "quận 12", "quận12", "Quận12", "12"]
        QTD = ["Quận Thủ Đức", "Q Thủ Đức", "q Thủ Đức", "quận Thủ Đức", "quận Thủ Đức", "Quận Thu Đuc", "Thu Duc", "Thủ Duc", "Thu Đức", "Thu Đưc","quận thủ đức", "Q thủ đức", "q thủ đức", "quận thủ đức", "quận thủ đức", "Quận thu duc", "thu duc", "thủ duc", "thu đức", "thu đưc"]
        QTBinh = ["Quận Tân Bình", "Q Tân Bình", "q Tân Bình", "quận Tân Bình", "quận Tân Bình", "Quận TB", "Tan Binh", "Tân Binh", "Tan Bình", "tan binh", "tân bình"]
        QBThanh = ["Quận Bình Tân", "QBình Tân", "qBình Tân", "quận Bình Tân", "quậnBình Tân", "QuậnBình Tân", "Bình Tân", "q bình tân", "quận bình tân", "q binh tan"]
        QBTan = ["Quận Bình Tân", "QBình Tân", "qBình Tân", "quận Bình Tân", "quậnBình Tân", "QuậnBình Tân", "bình tân","Quận bình tân", "Qbình tân", "qan", "quận bình tân", "quậnbình tân", "Quậnbình tân", "bình tân"]
        QPN = ["Quận Phú Nhuận", "QPhú Nhuận", "qPhú Nhuận", "quận Phú Nhuận", "quậnPhú Nhuận", "QuậnPhú Nhuận", "phú nhuận","quận phú nhuận", "q phú nhuận", "qPhú Nhuận", "quận Phú Nhuận", "quậnPhú Nhuận", "QuậnPhú Nhuận", "Phú Nhuận"]
        
        districtFind = "1"
        print(district)
        
        for i,value in enumerate(Q1):
            if district == value :
                districtFind = "1"
                break
        for i,value in enumerate(Q2):
            if district == value :
                districtFind = "2"
                break
        for i,value in enumerate(Q3):
            if district == value :
                districtFind = "3"
                break
        for i,value in enumerate(Q4):
            if district == value :
                districtFind = "4"
                break
        for i,value in enumerate(Q5):
            if district == value :
                districtFind = "5"
                break
        for i,value in enumerate(Q6):
            if district == value :
                districtFind = "6"
                break
        for i,value in enumerate(Q7):
            if district == value :
                districtFind = "7"
                break
        for i,value in enumerate(Q8):
            if district == value :
                districtFind = "8"
                break
        for i,value in enumerate(Q9):
            if district == value :
                districtFind = "9"
                break
        for i,value in enumerate(Q10):
            if district == value :
                districtFind = "10"
                break
        for i,value in enumerate(Q11):
            if district == value :
                districtFind = "11"
                break
        for i,value in enumerate(Q12):
            if district == value :
                districtFind = "12"
                break
        for i,value in enumerate(QBThanh):
            if district == value :
                districtFind = "B%C3%ACnh%20Th%E1%BA%A1nh"
                break
        for i,value in enumerate(QBTan):
            if district == value :
                districtFind = "BA%ADn%20B%C3%ACnh%20T%C3%A2n"
                break
        for i,value in enumerate(QTBinh):
            if district == value :
                districtFind = "T%C3%A2n%20B%C3%ACnh"
                break
        for i,value in enumerate(QPN):
            if district == value :
                districtFind = "Ph%C3%BA%20Nhu%E1%BA%ADn"
                break 
        for i,value in enumerate(QTD):
            if district == value :
                districtFind = "Th%E1%BB%A7%20%C4%90%E1%BB%A9c"
                break 
        
        URL ="http://localhost:3001/hotels?filter=%7B%22where%22%20%3A%20%7B%22address%22%20%3A%20%22Qu%E1%BA%ADn%20{}%22%7D%7D".format(districtFind)
         
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        response = requests.get(url = URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            # image = value["image"]
            image = value["image"]
            discount = value["discount"]
            address = value["address"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nĐịa chỉ: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), address,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nĐịa chỉ: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), address,star, Star(star)),
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                       "title": "Chi tiết"
                                   },
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
    
class ActionFindStarHotels(Action):
    def name(self):
        return "action_hotels_star"
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
        response = requests.get(url = URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
    
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            # image = value["image"]
            image = value["image"]
            discount = value["discount"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                       "title": "Chi tiết"
                                   },
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
    
class ActionFindMinHotels(Action):
    def name(self):
        return "action_hotels_min"
    async def run(self, dispatcher, tracker, domain):
        filterMin = tracker.get_slot('min')
        print('rẻ nhất')
        URL ="http://localhost:3001/hotels?filter=%7B%0A%0A%20%20%22order%22%3A%20%22price%20ASC%22%2C%0A%20%20%22where%22%20%3A%20%7B%22price%22%20%3A%20%7B%0A%20%20%22lte%22%3A%201000000%0A%7D%7D%0A%7D"

        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        # URL = "http://localhost:3001/hotels"
        # PARAM1 = '{"where": {"star": "3" }}'
        # PARAMS = { "filter": "{}".format(PARAM1)  }
        response = requests.get(url = URL)
        jsonResponse = response.json()
        # print(PARAM0)
        _elements = "",
        _tempsElements = "",
        
        for index in range(10):  
            name = jsonResponse[index]["name"]
            price = jsonResponse[index]["price"]
            # image = jsonResponse[index]["image"]
            image = jsonResponse[index]["image"]
            discount = jsonResponse[index]["discount"]
            star = jsonResponse[index]["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                       "title": "Chi tiết"
                                   },
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

class ActionFindMaxHotels(Action):
    def name(self):
        return "action_hotels_max"
    async def run(self, dispatcher, tracker, domain):
        filterMax = tracker.get_slot('max')
    
        URL ="http://localhost:3001/hotels?filter=%7B%0A%0A%20%20%22order%22%3A%20%22price%20DESC%22%2C%0A%20%20%22where%22%20%3A%20%7B%22price%22%20%3A%20%7B%0A%20%20%22gte%22%3A%201000000%0A%7D%7D%0A%7D"
         
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        # URL = "http://localhost:3001/hotels"
        # PARAM1 = '{"where": {"star": "3" }}'
        # PARAMS = { "filter": "{}".format(PARAM1)  }
        response = requests.get(url = URL)
        jsonResponse = response.json()
        # print(PARAM0)
        _elements = "",
        _tempsElements = "",
        
        for index,value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            # image = value["image"]
            image = value["image"]
            discount = value["discount"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                       "title": "Chi tiết"
                                   },
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
    
class ActionFindMinPriceHotels(Action):
    def name(self):
        return "action_hotels_min_price"
    async def run(self, dispatcher, tracker, domain):
        filterMinPrice = tracker.get_slot('price')
        # def hasNumbers(inputString):
        #     return bool(re.search(r'k', inputString))
        # # print(filterMinPrice)
        # if(hasNumbers(filterMinPrice) == True):
        #     print(True)
        # else :
        #     print(False)    

        # price = [""]
        # for i,value in enumerate(Q1):
        #        if district == value :
        #        districtFind = "1"
        #        break
        URL ="http://localhost:3001/hotels?filter=%7B%0A%0A%20%20%22order%22%3A%20%22price%20ASC%22%2C%0A%20%20%22where%22%20%3A%20%7B%22price%22%20%3A%20%7B%0A%20%20%22lte%22%3A%20{}%0A%7D%7D%0A%7D".format(filterMinPrice)
        print('dưới')
        
        
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        response = requests.get(url = URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        for index,value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            image = value["image"]
            image = value["image"]
            discount = value["discount"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                         
                        ]
                    },
            else:
                _elements += {
                               "title": "{}. {}".format(index+1,name),
                               "image_url": "{}".format(image),
                               "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                               "buttons": [
                                   {
                                       "type": "web_url",
                                       "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                       "title": "Chi tiết"
                                   },
                                 
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
    
class ActionFindMaxPriceHotels(Action):
    def name(self):
        return "action_hotels_max_price"
    async def run(self, dispatcher, tracker, domain):
        filterMaxPrice = tracker.get_slot('price')
        print(filterMaxPrice)
        print('trên')
        URL ="http://localhost:3001/hotels?filter=%7B%0A%0A%20%20%22order%22%3A%20%22price%20ASC%22%2C%0A%20%20%22where%22%20%3A%20%7B%22price%22%20%3A%20%7B%0A%20%20%22gte%22%3A%20{}%0A%7D%7D%0A%7D".format(filterMaxPrice)
         
        def Star(star):
            temp = round(float(star) + 0.1)
            a = '' 
            b = ''
            for x in range(temp):
                a = a + '⭑'
            for x in range(5 - temp):
                b = b + '⭒'
            return a + b
        
        response = requests.get(url = URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            price = value["price"]
            # image = value["image"]
            image = value["image"]
            discount = value["discount"]
            star = value["star"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giá: {} VND\nDiscount: {}\nĐánh giá: {} {}".format('{:7,.0f}'.format(price), discount,star, Star(star)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://mytour.vn/c3/khach-san-4-sao-tai-ho-chi-minh.html",
                                "title": "Chi tiết"
                            },
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
    
class ActionRestaurants(Action):
    def name(self):
        return "action_restaurants"
    async def run(self, dispatcher, tracker, domain):
        response = requests.get("http://localhost:3001/restaurants")
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index in range(10):  
            name = jsonResponse[index]["name"]
            openTime = jsonResponse[index]["openTime"]
            priceRef = '{:7,.0f}'.format(jsonResponse[index]["lowestPrice"]) +' - ' + '{:7,.0f}'.format(jsonResponse[index]["highestPrice"])
            address = jsonResponse[index]["address"]
            image = jsonResponse[index]["image"]
            review = jsonResponse[index]["review"]
            district = jsonResponse[index]["district"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                "title": "Chi tiết"
                            },
                            {
                                "type" : "web_url",
                                "url" : address,
                                "title": "Chỉ đường"
                            }
                        ]
                    },
            else:
                _elements += {
                                "title": "{}. {}".format(index+1,name),
                                "image_url": "{}".format(image),
                                "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district),
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                        "title": "Chi tiết"
                                    },
                                    {
                                        "type": "web_url",
                                        "url": address,
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
    
class ActionRestaurantsDistrict(Action):
    def name(self):
        return "action_restaurants_district"
    async def run(self, dispatcher, tracker, domain):
        district = tracker.get_slot('res_district')
        Q1 = ["Quận 1", "Q1", "q1", "quận 1", "quận1", "Quận1", "1"]
        Q2 = ["Quận 2", "Q2", "q2", "quận 2", "quận2", "Quận2", "2"]
        Q3 = ["Quận 3", "Q3", "q3", "quận 3", "quận3", "Quận3", "3"]
        Q4 = ["Quận 4", "Q4", "q4", "quận 4", "quận4", "Quận4", "4"]
        Q5 = ["Quận 5", "Q5", "q5", "quận 5", "quận5", "Quận5", "5"]
        Q6 = ["Quận 6", "Q6", "q6", "quận 6", "quận6", "Quận6", "6"]
        Q7 = ["Quận 7", "Q7", "q7", "quận 7", "quận7", "Quận7", "7"]
        Q8 = ["Quận 8", "Q8", "q8", "quận 8", "quận8", "Quận8", "8"]
        Q9 = ["Quận 9", "Q9", "q9", "quận 9", "quận9", "Quận9", "9"]
        Q10 = ["Quận 10", "Q10", "q10", "quận 10", "quận10", "Quận10", "10"]
        Q11 = ["Quận 11", "Q11", "q11", "quận 11", "quận11", "Quận11", "11"]
        Q12 = ["Quận 12", "Q12", "q12", "quận 12", "quận12", "Quận12", "12"]
        QTD = ["Quận Thủ Đức", "Q Thủ Đức", "q Thủ Đức", "quận Thủ Đức", "quận Thủ Đức", "Quận Thu Đuc", "Thu Duc", "Thủ Duc", "Thu Đức", "Thu Đưc","quận thủ đức", "Q thủ đức", "q thủ đức", "quận thủ đức", "quận thủ đức", "Quận thu duc", "thu duc", "thủ duc", "thu đức", "thu đưc"]
        QTBinh = ["Quận Tân Bình", "Q Tân Bình", "q Tân Bình", "quận Tân Bình", "quận Tân Bình", "Quận TB", "Tan Binh", "Tân Binh", "Tan Bình", "tan binh", "tân bình"]
        QBThanh = ["Quận Bình Tân", "QBình Tân", "qBình Tân", "quận Bình Tân", "quậnBình Tân", "QuậnBình Tân", "Bình Tân", "q bình tân", "quận bình tân", "q binh tan"]
        QBTan = ["Quận Bình Tân", "QBình Tân", "qBình Tân", "quận Bình Tân", "quậnBình Tân", "QuậnBình Tân", "bình tân","Quận bình tân", "Qbình tân", "qan", "quận bình tân", "quậnbình tân", "Quậnbình tân", "bình tân"]
        QPN = ["Quận Phú Nhuận", "QPhú Nhuận", "qPhú Nhuận", "quận Phú Nhuận", "quậnPhú Nhuận", "QuậnPhú Nhuận", "phú nhuận","quận phú nhuận", "q phú nhuận", "qPhú Nhuận", "quận Phú Nhuận", "quậnPhú Nhuận", "QuậnPhú Nhuận", "Phú Nhuận"]
        
        districtFind = "1"
        print(district)
        
        for i,value in enumerate(Q1):
            if district == value :
                districtFind = "1"
                break
        for i,value in enumerate(Q2):
            if district == value :
                districtFind = "2"
                break
        for i,value in enumerate(Q3):
            if district == value :
                districtFind = "3"
                break
        for i,value in enumerate(Q4):
            if district == value :
                districtFind = "4"
                break
        for i,value in enumerate(Q5):
            if district == value :
                districtFind = "5"
                break
        for i,value in enumerate(Q6):
            if district == value :
                districtFind = "6"
                break
        for i,value in enumerate(Q7):
            if district == value :
                districtFind = "7"
                break
        for i,value in enumerate(Q8):
            if district == value :
                districtFind = "8"
                break
        for i,value in enumerate(Q9):
            if district == value :
                districtFind = "9"
                break
        for i,value in enumerate(Q10):
            if district == value :
                districtFind = "10"
                break
        for i,value in enumerate(Q11):
            if district == value :
                districtFind = "11"
                break
        for i,value in enumerate(Q12):
            if district == value :
                districtFind = "12"
                break
        for i,value in enumerate(QBThanh):
            if district == value :
                districtFind = "B%C3%ACnh%20Th%E1%BA%A1nh"
                break
        for i,value in enumerate(QBTan):
            if district == value :
                districtFind = "BA%ADn%20B%C3%ACnh%20T%C3%A2n"
                break
        for i,value in enumerate(QTBinh):
            if district == value :
                districtFind = "T%C3%A2n%20B%C3%ACnh"
                break
        for i,value in enumerate(QPN):
            if district == value :
                districtFind = "Ph%C3%BA%20Nhu%E1%BA%ADn"
                break 
        for i,value in enumerate(QTD):
            if district == value :
                districtFind = "Th%E1%BB%A7%20%C4%90%E1%BB%A9c"
                break 
            
        URL = "http://localhost:3001/restaurants?filter=%7B%22where%22%20%3A%20%7B%22district%22%20%3A%20%22Qu%E1%BA%ADn%20{}%22%7D%7D".format(districtFind)
        response = requests.get(URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            openTime = value["openTime"]
            priceRef = '{:7,.0f}'.format(value["lowestPrice"]) +' - ' + '{:7,.0f}'.format(value["highestPrice"])
            address = value["address"]
            image = value["image"]
            review = value["review"]
            district = value["district"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                "title": "Chi tiết"
                            },
                            {
                                "type" : "web_url",
                                "url" : address,
                                "title": "Chỉ đường"
                            }
                        ]
                    },
            else:
                _elements += {
                                "title": "{}. {}".format(index+1,name),
                                "image_url": "{}".format(image),
                                "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district, review),
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                        "title": "Chi tiết"
                                    },
                                    {
                                        "type" : "web_url",
                                        "url" : address,
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

class ActionRestaurantsType(Action):
    def name(self):
        return "action_restaurants_type"
    async def run(self, dispatcher, tracker, domain):
        LAU = ["lau", "lẩu", "Lẩu", "Lau"]
        PHO = ["Phở", "phở", "Pho", "pho"]
        BUN = ["Bún", "bun", "Bun", "bún"]
        typeTravel = tracker.get_slot('type_res')
        findType = "L%E1%BA%A9u"
        for i,value in enumerate(LAU):
            if typeTravel == value :
                findType = "L%E1%BA%A9u"
                break
        for i,value in enumerate(PHO):
            if typeTravel == value :
                findType = "ph%E1%BB%9F"
                break
        for i,value in enumerate(BUN):
            if typeTravel == value :
                findType = "b%C3%BAn"
                break
        print(typeTravel)
        print(findType)
        URL = "http://localhost:3001/restaurants?filter=%20%7B%22where%22%3A%20%7B%22name%22%3A%20%7B%22ilike%22%3A%20%22{}%22%7D%7D%7D".format(findType)
        response = requests.get(URL)
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index, value in enumerate(jsonResponse):  
            name = value["name"]
            openTime = value["openTime"]
            priceRef = '{:7,.0f}'.format(value["lowestPrice"]) +' - ' + '{:7,.0f}'.format(value["highestPrice"])
            address = value["address"]
            image = value["image"]
            review = value["review"]
            district = value["district"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                "title": "Chi tiết"
                            },
                            {
                                "type" : "web_url",
                                "url" : address,
                                "title": "Chỉ đường"
                            }
                        ]
                    },
            else:
                _elements += {
                                "title": "{}. {}".format(index+1,name),
                                "image_url": "{}".format(image),
                                "subtitle": "Giờ mở cửa: {}\nGiá tham khảo:{} VNĐ\nĐịa chỉ: {}".format(openTime, priceRef, district, review),
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.vntrip.vn/cam-nang/cac-mon-am-thuc-sai-gon-21909",
                                        "title": "Chi tiết"
                                    },
                                    {
                                        "type" : "web_url",
                                        "url" : address,
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
    
class ActionHello(Action):
    def name(self):
        return "action_hello"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Chào mừng bạn đến với Du Lịch Ở Đâu",
                    "image_url":"https://d3jyiu4jpn0ihr.cloudfront.net/wp-content/uploads/sites/6/20190918160006/ve-may-bay-di-sai-gon1.jpg",
                    "subtitle":"Mình có thể giúp gì được cho bạn ?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Tour du lịch",
                        "payload":"/tour"
                    },{
                        "type":"postback",
                        "title":"Địa điểm phổ biến",
                        "payload":"/choose_type"
                    },{
                        "type":"postback",
                        "title":"Hỏi đáp",
                        "payload":"/faq"
                    }               
                    ]      
                }
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return []   

class ActionChooseType(Action):
    def name(self):
        return "action_choose_type"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Du lịch, Ẩm thưc, Khách sạn",
                    "image_url":"https://mytourcdn.com/upload_images/Image/Location/3_9_2015/cac-dia-diem-du-lich-sai-gon-mytour-1.jpg",
                    "subtitle":"Mình có thể giúp gì được cho bạn ?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Địa điểm du lịch",
                        "payload":"/placeTravel_topTravelDestination"
                    },{
                        "type":"postback",
                        "title":"Ẩm thực",
                        "payload":"/restaurants"
                    },{
                        "type":"postback",
                        "title":"Khách sạn",
                        "payload":"/hotels"
                    }               
                    ]      
                }
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return []  
    
class ActionFAQ(Action):
    """ Return today's weather forecast"""
    def name(self):
        return "action_faq"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Thời tiết",
                    "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFFl8hGoWznFMiZyUs2RLvgyZ_nGE3GhjBGQ&usqp=CAU",
                    "subtitle":"Thời tiết nơi đây?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/weather_city_forecasts"
                    }           
                    ]      
                },
                {
                    "title":"Phương tiện",
                    "image_url":"https://vemaybayphuongnam.net/assets/uploads/2019/03/nen-di-tau-hoa-hay-may-bay-600x400.jpg",
                    "subtitle":"Đi bằng gì?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/vehicle"
                    }           
                    ]      
                },
                {
                    "title":"Thời điểm",
                    "image_url":"https://previews.123rf.com/images/zeinousstudio/zeinousstudio2005/zeinousstudio200500008/146862981-time-to-travel-vector-concept-design-time-to-travel-text-in-globe-with-travelling-and-world-country-.jpg",
                    "subtitle":"Đi lúc nào?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/time"
                    }           
                    ]      
                },{
                    "title":"Sự kiện",
                    "image_url":"https://cdn.vietnambiz.vn/2020/2/18/lhvn-15820195320031413059532.jpg",
                    "subtitle":"Lễ hội đặc sắc?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/event"
                    }           
                    ]      
                },{
                    "title":"Văn hoá",
                    "image_url":"https://cdn.vietnamtours247.com/2020/02/sai-gon-xua-va-nay-co-gi-thu-vi.png",
                    "subtitle":"Văn hoá nơi đây?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/culture"
                    }           
                    ]      
                },{
                    "title":"Quà lưu niệm",
                    "image_url":"https://mavang.vn/wp-content/uploads/2017/03/Cho_BT_4.jpg",
                    "subtitle":"Mua gì - ở đâu?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/souvenir"
                    }           
                    ]      
                },{
                    "title":"Lưu ý",
                    "image_url":"http://tnttravel.tnt-vietnam.com/uploads/news/2016/08/10/pic-1_750_506.jpg",
                    "subtitle":"Những điều nên và không nên?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/note"
                    }           
                    ]      
                },{
                    "title":"Trang phục",
                    "image_url":"https://katchup.vn/asset/upload/bai-viet/tai-lieu/tieng-anh/tu-vung-tieng-anh-chu-de-quan-ao-1.gif",
                    "subtitle":"Mặc gì bây giờ?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/skin"
                    }           
                    ]      
                },
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return []  
    
class ActionVehicleDetail(Action):
    def name(self):
        return "action_vehicle_detail"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Di chuyển tới Sài Gòn",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/23/phuong-tien-du-lich-sai-gon-mytour-1.jpg",
                    "subtitle":"Đi bằng gì tới Sài Gòn",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/vehicleToSG"
                    }       
                    ]      
                },{
                    "title":"Di chuyển trong Sài Gòn",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/23/phuong-tien-du-lich-sai-gon-mytour-5.jpg",
                    "subtitle":"Di chuyển trong Sài Gòn bằng gì?",
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Chi tiết",
                        "payload":"/vehicleInSG"
                    }       
                    ]      
                }
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return [] 

class ActionEvent(Action):
    """ Return today's weather forecast"""
    def name(self):
        return "action_event"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Phối cảnh đường hoa Nguyễn Huệ",
                    "image_url":"https://i1-vnexpress.vnecdn.net/2021/01/16/duong-hoa-1-1610359516-6797-1610772728.jpg?w=680&h=0&q=100&dpr=2&fit=crop&s=R300FMlzC0A7SbQlSY7yzg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
                {
                    "title":"Biểu diễn trước Nhà hát Thành phố",
                    "image_url":"https://nld.mediacdn.vn/2021/1/21/13-chot-1611239298564109689413.jpg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
                {
                    "title":"Ngày hội Bánh tét",
                    "image_url":"https://media.travelmag.vn/files/thuhang/2021/01/18/7-2205.jpg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
                {
                    "title":"Hội hoa Xuân Tao Đàn",
                    "image_url":"https://media.travelmag.vn/files/thuhang/2021/01/18/8-2207.jpg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
                {
                    "title":"Chợ hoa Tết",
                    "image_url":"https://media.travelmag.vn/files/thuhang/2021/01/18/10-2208.jpg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
                {
                    "title":"Lễ hội và hoạt động khác",
                    "image_url":"https://media.travelmag.vn/files/thuhang/2021/01/18/11-2211.jpg",
                    "subtitle":"",
                    "buttons":[
                      {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },        
                    ]      
                },
               
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return []      
    
class ActionSouvenir(Action):
    """ Return today's weather forecast"""
    def name(self):
        return "action_souvenir"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"TRÀ PHÚC LONG",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/20/qua-du-lich-sai-gon-mytour-1.jpg",
                    "subtitle":"",
                    "buttons":[
                     {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },       
                    ]      
                },
                {
                    "title":"DẠO CHỢ BẾN THÀNH SẮM ĐỒ LÀM QUÀ",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/20/qua-du-lich-sai-gon-mytour-6.jpg",
                    "subtitle":"",
                    "buttons":[
                     {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },       
                    ]      
                },
                {
                    "title":"NHỮNG THIÊN ĐƯỜNG MUA SẮM HÀNG HIỆU",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/21/qua-du-lich-sai-gon-mytour-10.jpg",
                    "subtitle":"",
                    "buttons":[
                     {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },       
                    ]      
                },
                {
                    "title":"ĐỘC ĐÁO MÓN QUÀ TỰ TAY LÀM BẰNG GỐM",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location/21_7_2016/21/qua-du-lich-sai-gon-mytour-12.jpg",
                    "subtitle":"",
                    "buttons":[
                     {
                                    "type": "web_url",
                                    "url": "https://vnexpress.net/loat-su-kien-mung-tet-tan-suu-o-sai-gon-4221998.html",
                                    "title": "Chi tiết"
                                },       
                    ]      
                },
               
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return [] 

class ActionTour(Action):
    def name(self):
        return "action_tour"
    async def run(self, dispatcher, tracker, domain):
        response = requests.get("http://localhost:3001/tours")
        jsonResponse = response.json()
        _elements = "",
        _tempsElements = "",
        
        for index in range(10):  
            name = jsonResponse[index]["name"]
            time = jsonResponse[index]["time"]
            image = jsonResponse[index]["image"]
            departure = jsonResponse[index]["departure"]
            price = jsonResponse[index]["price"]
            url = jsonResponse[index]["url"]
            if _elements == _tempsElements:
                _elements = {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Thời gian: {}\nĐiểm khởi hành: {}\nGiá: {} VNĐ".format(time, departure,'{:7,.0f}'.format(price)),

                        "buttons": [
                            {
                                "type": "web_url",                                "url": url,
                                "title": "Chi tiết"
                            },
                        ]
                    },
            else:
                _elements += {
                        "title": "{}. {}".format(index+1,name),
                        "image_url": "{}".format(image),
                        "subtitle": "Thời gian: {}\nĐiểm khởi hành: {}\nGiá: {} VNĐ".format(time, departure,'{:7,.0f}'.format(price)),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": url,
                                "title": "Chi tiết"
                            },
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
    
class ActionNote(Action):
    """ Return today's weather forecast"""
    def name(self):
        return "action_note"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"SÀI GÒN HAI MÙA: NÓNG VÀ NÓNG HƠN NỮA",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%201/luu-y-khi-du-lich-sg-mytour-1.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"CẨN THẬN BỊ THỔI PHẠT VÌ ĐI NHẦM ĐƯỜNG MỘT CHIỀU",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%201/luu-y-khi-du-lich-sg-mytour-6.jpg",
                    "subtitle":"",
                    "buttons":[
                    {   
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"LUÔN CẨN THẬN VỚI TƯ TRANG KHI DẠO PHỐ",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%201/luu-y-khi-du-lich-sg-mytour-10.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"CẨN TRỌNG VỚI ẨM THỰC ĐƯỜNG PHỐ",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%202/luu-y-khi-du-lich-sg-mytour-11.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"TRÁNH GIỜ CAO ĐIỂM, NÉ CẢNH ÁCH TẮC NGƯỜI XE",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%202/luu-y-khi-du-lich-sg-mytour-15.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },{
                    "title":"THÔNG MINH KHI MUA HÀNG, NGHỆ THUẬT MẶC CẢ",
                    "image_url":"https://s3-ap-southeast-1.amazonaws.com/mytour-static-file/upload_images/Image/Location%20Articles/Luu%20y%20Sai%20Gon%202/luu-y-khi-du-lich-sg-mytour-20.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://mytour.vn/c3/477-nhung-dieu-can-luu-y-khi-du-lich-sai-gon.html",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
               
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return [] 
    
class ActionSkin(Action):
    """ Return today's weather forecast"""
    def name(self):
        return "action_skin"
    def run(self, dispatcher, tracker, domain):
        gt =    {
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"generic",
                "elements":[
                {
                    "title":"Trang phục đi tham quan, sống ảo",
                    "image_url":"https://cattour.vn/images/upload/images/quy-nhon/di-du-lich-quy-nhon-mac-gi-de-co-nhung-bo-anh-song-ao-cuc-chat/diquynhonmacgi1.png",
                    "subtitle":"",
                    "buttons":[
                    {
                        "type": "web_url",
                        "url":"https://list.vn/san-lung-25-shop-quan-ao-ban-do-dep-van-nguoi-follow-hot-nhat-sai-gon/",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"Phối đồ cùng mũ nón để sống ảo",
                    "image_url":"https://cdn.vietnamtours247.com/2019/07/mac-gi-khi-du-lich-da-nang-03.png",
                    "subtitle":"",
                    "buttons":[
                    {
                         "type": "web_url",
                        "url":"https://list.vn/san-lung-25-shop-quan-ao-ban-do-dep-van-nguoi-follow-hot-nhat-sai-gon/",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"Áo phông, quần jean thoải mái dạo phố",
                    "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtriu_mr8KKEUWFKOpAY3Id-Li0bubQ8w61w&usqp=CAU",
                    "subtitle":"",
                    "buttons":[
                    {
                         "type": "web_url",
                        "url":"https://list.vn/san-lung-25-shop-quan-ao-ban-do-dep-van-nguoi-follow-hot-nhat-sai-gon/",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
                {
                    "title":"Lựa chọn trang phục đi dã ngoại",
                    "image_url":"https://timeoutvietnam.com/files/2016/04/07/mot-chuyen-di-rung-trong-toi-3.jpg",
                    "subtitle":"",
                    "buttons":[
                    {
                         "type": "web_url",
                        "url":"https://list.vn/san-lung-25-shop-quan-ao-ban-do-dep-van-nguoi-follow-hot-nhat-sai-gon/",
                        "title": "Chi tiết",
                    }           
                    ]      
                },
               
                ]
            }
            }
        }
        dispatcher.utter_custom_json(gt)                                           
        return [] 