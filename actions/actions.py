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

import requests


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hello = "hihi"
        
        dispatcher.utter_message(hello)
        return []


class ActionGetWeather(Action):

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):

        city = tracker.get_slot('location')
        api_token = "417d2d3d5443b9068b0580a5e3414961"
        url = "api.openweathermap.org/data/2.5/weather"
        payload = {"q": city, "appid": api_token, "units": "metric", "lang": "vi"}
        response = requests.get(url, params=payload)
        if response.ok:
            description = response.json()["weather"][0]["description"]
            temp = round(response.json()["main"]["temp"])
            cityGR = response.json()["name"]

            msg = f"Nhiệt độ hiện tại của {cityGR} là {temp} độ C. Dự báo hôm nay trời sẽ {description}"
        else:
            msg= "Xin vui lòng nhập lại, đã xảy ra lỗi với thành phố được yêu cầu."

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]

    
