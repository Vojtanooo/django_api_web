from django import template
from random import randint

register = template.Library()


@register.filter
def question(value):
    context = value
    return context["question"]


@register.filter
def answers(value):
    context = value
    correct = context["correct_answer"]
    answers = context["incorrect_answers"]

    lst = answers
    lst.insert(randint(0, 3), correct)
    return lst
