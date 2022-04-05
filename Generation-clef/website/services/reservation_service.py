import json
import requests


def list_reservations(request):
    reservations = requests.get(
        f"http://localhost:8000/api/v1/reservations/",
        params=request.GET,
    ).text

    return json.loads(reservations)
