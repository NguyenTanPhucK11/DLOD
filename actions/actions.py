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

            msg = f"Nhiệt độ hiện tại tại {city} là {temp} độ C và {description}"
        else:
            msg= "Lỗi!"

        dispatcher.utter_message(msg)
        return [SlotSet("location", None)]
class GetName(Action):
    def name(self):
	    return 'action_name'
		
    def run(self, dispatcher, tracker, domain):
		
        most_recent_state = tracker.current_state()
        sender_id = most_recent_state['sender_id']

        r = requests.get('https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}'.format(sender_id, fb_access_token)).json()
        first_name = r['first_name']
        last_name = r['last_name']
        print(first_name)
        return [SlotSet('name', first_name), SlotSet('surname', last_name)]
class ActionTest(Action):
    
    def name(self):
        return "action_api"

    def run(self, dispatcher, tracker, domain):
        response = requests.get("http://192.168.100.44:3000/place-travels")
        jsonResponse = response.json()
        # print(jsonResponse)
        # listPlaceTravel = map(lambda item: item.name, jsonResponse)
        
        # print(listPlaceTravel)
        # print(list(listPlaceTravel))
        # json_string = json.dumps(jsonResponse)
        # print(json_string)
        # test_list = [1, 4, 5, 6, 7]
        for index, value in enumerate(jsonResponse):
            name = value["name"]
            type = value["type"]
            review = value["review"]
            messageToUser = "{}. {} \n {} \n ⭐⭐⭐⭐{}\n".format(index +1 ,name, type, review)
            dispatcher.utter_message(messageToUser)
        # title = jsonResponse[0]["name"]
        # id = jsonResponse[0]["id"]

        # messageToUser = "id2 là \"{}\" và title là \"{}\"".format(id, title)
        # dispatcher.utter_message(messageToUser)

        return []
    
