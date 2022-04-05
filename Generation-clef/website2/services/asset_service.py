import json
import requests


def list_assets(request):
    assets = requests.get(
        f"http://localhost:8000/api/v1/assets/",
        params=request.GET,
    ).text

    return json.loads(assets)


def get_asset(request, id_):
    asset = requests.get(
        f"http://localhost:8000/api/v1/assets/{id_}/",
        params=request.GET,
    ).text

    return json.loads(asset)


def create_asset(request, user_id):
    payload = {
        "user_id": user_id,
        "name": request.POST["add_asset_name"],
        "description": request.POST["add_asset_description"],
        "image_url": "temp_url",
    }
    requests.post(f"http://localhost:8000/api/v1/assets/", data=payload)
