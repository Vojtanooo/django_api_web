import requests
import json


def api():
    api = requests.get(
        "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium").json()["results"]
    with open("request_api.json", "w") as json_file:
        json.dump(api, json_file)
