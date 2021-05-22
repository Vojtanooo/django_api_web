from django.shortcuts import redirect, render
from .get_api import get_question, api
from .models import Leaderboard
from django.contrib import messages
from .get_leaderboard import get_leaderboard


def quiz(request):
    context = {
        "context": get_question(0)[0],
        "username": request.session.get("username"),
        "score": request.session.get("score")
    }

    if request.session["num"] == 9:
        return redirect("finish-page")

    if request.method == "POST":
        num = request.session.get("num") + 1
        request.session["num"] = num

        if request.POST.get("button") in get_question(0)[1]:
            score = request.session.get("score") + 1
            request.session["score"] = score
            context.update({"context": get_question(num)[0], "score": score})
        else:
            context.update({"context": get_question(num)[0]})

    return render(request, "quiz.html", context)


def starting_page(request):
    if "submit" in request.POST:
        api(request.POST.get("category"), request.POST.get("difficulty"))

        if Leaderboard.objects.filter(username=request.POST.get("username")):
            redirect("starting-page")
            messages.warning(
                request, "Username is already taken...Try another")
        else:
            request.session["username"] = request.POST.get("username")
            request.session["score"] = 0
            request.session["num"] = 0
            return redirect("quiz")
    return render(request, "starting_page.html")


def finish_page(request):
    username = request.session.get("username")
    score = request.session.get("score")
    Leaderboard.objects.create(username=username.lower(), score=score)
    request.session.clear()

    return render(request, "finish_page.html", {"username": username, "score": score})


def leaderboard(request):
    username_score = get_leaderboard()

    return render(request, "leaderboard.html", {"username_score": username_score})
