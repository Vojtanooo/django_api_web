from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('quiz', views.quiz, name='quiz'),
    path('', views.starting_page, name='starting-page'),
    path('finish', views.finish_page, name="finish-page"),
    path('leaderboard', views.leaderboard, name="leaderboard")
]
