from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden

from .services.user_service import list_users, get_user, login_user, register_user
from .services.wallet_service import create_wallet, list_wallets, get_wallet
from .services.vote_service import create_vote, list_vote, get_vote


def index(request):
    context = {"title": "Acceuil"}
    return render(request, "website/index.html", context)


def postings(request):
    context = {"title": "Annonces"}
    return render(request, "website/postings.html", context)

def view_key(request, user_id):
    user = get_user(request, user_id)
    wallets = list_wallets(request)
    context = {"title": "Securite", "user": user, "wallets": wallets}
    return render(request, "website/view_key.html", context)

def view_key2(request, user_id):
    user = get_user(request, user_id)
    wallets = list_wallets(request)
    context = {"title": "Securite", "user": user, "wallets": wallets}
    return render(request, "website/view_key2.html", context)

def vote(request, user_id):
    user = get_user(request, user_id)
    wallets = list_wallets(request)
    context = {"title": "Vote", "user": user, "wallets": wallets}
    return render(request, "website/vote.html", context)

def vote2(request, user_id):
    user = get_user(request, user_id)
    vote = list_vote(request)
    context = {"title": "Vote", "user": user, "votes": vote}
    return render(request, "website/vote2.html", context)

# ? Users
def register(request):
    if request.method == "GET":
        context = {"title": "Inscription"}

        return render(request, "website/inscription.html", context)

    elif request.method == "POST":
        register_user(request)

        return redirect("index")


def login(request):
    if request.method == "GET":
        context = {"title": "Connexion"}

        return render(request, "website/login.html", context)

    elif request.method == "POST":
        user = login_user(request)
        if user:
            id_, username = user["id"], user["username"]

            request.session["id_"] = id_
            request.session["username"] = username

            return redirect("index")
        else:
            request.session["invalid_user"] = True
            return redirect(request.path)


def logout(request):
    try:
        del request.session["id_"]
        del request.session["username"]
    except KeyError:
        pass

    return redirect("index")

def add_wallet(request, user_id):
    create_wallet(request, user_id)
    user = get_user(request, user_id)
    wallets = list_wallets(request)
    context = {"title": "Securite", "user": user, "wallets": wallets}
    return render(request, "website/view_key2.html", context)

def add_vote(request, user_id):
    create_vote(request, user_id)
    user = get_user(request, user_id)
    vote = list_vote(request)
    context = {"title": "Vote", "user": user, "votes": vote}
    return render(request, "website/vote2.html", context)

