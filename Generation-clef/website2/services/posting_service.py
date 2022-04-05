import json
import requests


def list_postings(request):
    postings = requests.get(
        "http://localhost:8000/api/v1/postings/", params=request.GET
    ).text

    return json.loads(postings)


def create_posting_req(request, asset_id):
    payload = {
        "asset_id": asset_id,
        "title": request.POST["create_posting_title"],
        "description": request.POST["create_posting_description"],
        "starting_date": request.POST["create_posting_starting_date"],
        "end_date": request.POST["create_posting_end_date"],
        "cost_per_day": request.POST["create_posting_cost_per_day"],
    }
    requests.post(f"http://localhost:8000/api/v1/postings/", data=payload)
