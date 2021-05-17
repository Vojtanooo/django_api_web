from typing import List
import requests
import json


def api(category, difficulty):
    api = requests.get(
        f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}").json()["results"]
    with open("request_api.json", "w") as json_file:
        json.dump(api, json_file)


def get_question(num):
    with open("request_api.json") as file:
        context = json.load(file)
    listek = [item["correct_answer"] for item in context]
    return context[num], listek
