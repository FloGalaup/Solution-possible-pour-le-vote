import json
import requests


def list_wallets(request):
    wallets = requests.get(
        f"http://localhost:8000/api/v1/wallets/",
        params=request.GET,
    ).text

    return json.loads(wallets)


def get_wallet(request, id_):
    wallet = requests.get(
        f"http://localhost:8000/api/v1/wallets/{id_}/",
        params=request.GET,
    ).text

    return json.loads(wallet)


def create_wallet(request, id_):
    wallet = {"user_id": id_}
    requests.post(f"http://localhost:8000/api/v1/wallets/", data=wallet)
