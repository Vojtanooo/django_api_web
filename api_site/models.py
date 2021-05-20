from django.db import models


class Leaderboard(models.Model):

    username = models.CharField(max_length=50, primary_key=True,)
    score = models.IntegerField()
