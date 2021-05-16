from typing import List
import requests
import json


def api():
    api = requests.get(
        "https://opentdb.com/api.php?amount=10&category=21&difficulty=medium").json()["results"]
    with open("request_api.json", "w") as json_file:
        json.dump(api, json_file)


def get_question(num):
    with open("request_api.json") as file:
        context = json.load(file)
    listek = [item["correct_answer"] for item in context]
    return context[num], listek
