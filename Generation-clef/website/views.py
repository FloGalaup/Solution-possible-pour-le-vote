from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden

from .services.asset_service import create_asset, get_asset, list_assets
from .services.reservation_service import list_reservations
from .services.posting_service import list_postings, create_posting_req
from .services.user_service import list_users, get_user, login_user, register_user
from .services.wallet_service import create_wallet, list_wallets, get_wallet
from .services.helpers import is_admin


def index(request):
    postings = list_postings(request)
    context = {"title": "Acceuil", "postings": postings}

    return render(request, "website/index.html", context)


def postings(request):
    context = {"title": "Annonces"}
    return render(request, "website/postings.html", context)


def about(request):
    context = {"title": "À Propos"}
    return render(request, "website/about.html", context)


def contact(request):
    context = {"title": "Contact"}
    return render(request, "website/contact.html", context)

def view_key(request, user_id):
    user = get_user(request, user_id)
    wallets = list_wallets(request)
    context = {"title": "Securite", "user": user, "wallets": wallets}
    return render(request, "website/view_key.html", context)


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
            id_, username, is_admin = user["id"], user["username"], user["is_admin"]

            request.session["id_"] = id_
            request.session["username"] = username
            request.session["is_admin"] = is_admin

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


def dashboard(request, user_id):
    if is_admin(request):
        user, wallet = get_user(request, user_id), get_wallet(
            request, user_id
        )  #! TEMP wallet id
        users, assets, postings, reservations, wallets = (
            list_users(request),
            list_assets(request),
            list_postings(request),
            list_reservations(request),
            list_wallets(request),
        )
        context = {
            "title": "Profil Administrateur",
            "user": user,
            "wallet": wallet,
            "users": users,
            "assets": assets,
            "postings": postings,
            "reservations": reservations,
            "wallets": wallets,
        }

        return render(request, "website/dashboard_admin.html", context)

    else:
        user= get_user(request, user_id)
        wallets = list_wallets(request)
        assets = list_assets(request)
        context = {"title": "Profil", "user": user, "wallets": wallets, "assets": assets}

        return render(request, "website/dashboard.html", context)


def add_wallet(request, user_id):
    create_wallet(request, user_id)

    if is_admin(request):
        return redirect("view_key", user_id)
    else:
        return redirect("view_key", user_id)


def create_posting(request, user_id, asset_id):
    if request.method == "GET":
        user, asset = get_user(request, user_id), get_asset(request, asset_id)
        context = {"title": "Annonces | Création", "user": user, "asset": asset}

        return render(request, "website/create_posting.html", context)

    elif request.method == "POST":
        create_posting_req(request, asset_id)

        if is_admin(request):
            return redirect("dashboard_admin", user_id)
        else:
            return redirect("dashboard", user_id)


def add_asset(request, user_id):
    if request.method == "GET":
        user = get_user(request, user_id)
        context = {"title": "Actifs | Ajout", "user": user}

        return render(request, "website/add_asset.html", context)

    elif request.method == "POST":
        create_asset(request, user_id)

        if is_admin(request):
            return redirect("dashboard_admin", user_id)
        else:
            return redirect("dashboard", user_id)
