import json
import requests


def list_users(request):
    users = requests.get(
        f"http://localhost:8000/api/v1/users/",
        params=request.GET,
    ).text

    return json.loads(users)


def get_user(request, id_):
    user = requests.get(
        f"http://localhost:8000/api/v1/users/{id_}/",
        params=request.GET,
    ).text

    return json.loads(user)


def register_user(request):
    user = {
        "username": request.POST["register_username"],
        "email": request.POST["register_email"],
        "password": request.POST["register_password"],
    }
    requests.post(f"http://localhost:8000/api/v1/users/", data=user)


def login_user(request):
    credentials = {
        "username": request.POST["login_username"],
        "password": request.POST["login_password"],
    }
    username = credentials["username"]

    user = requests.get(
        f"http://localhost:8000/api/v1/users/login/{username}/",
        params=request.GET,
    ).text

    user = json.loads(user)

    return user if credentials["password"] == user["password"] else None
