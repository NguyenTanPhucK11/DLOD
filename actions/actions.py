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

            msg = f"Nhiệt độ hiện tại tại {cityGR} là {temp} độ C và {description}"
        else:
            msg= "Lỗi!"

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]

class ActionTest(Action):
    
    def name(self):
        return "action_api"

    def run(self, dispatcher, tracker, domain):
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        jsonResponse = response.json()
        title = jsonResponse["title"]
        id = jsonResponse["id"]

        messageToUser = "id là \"{}\" và title là \"{}\"".format(id, title)
        dispatcher.utter_message(messageToUser)

        return []

    
