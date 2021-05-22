from .models import Leaderboard
from collections import Counter


def get_leaderboard():
    model = Leaderboard.objects.all()
    dict_of_objects = {}
    for item in model:
        dict_of_objects[f"{item.username}"] = f"{item.score}"
    return Counter(dict_of_objects).most_common()[:10]
