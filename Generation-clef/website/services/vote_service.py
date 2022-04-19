import json
import requests


def list_vote(request):
    vote = requests.get(
        f"http://localhost:8000/api/v1/votes/",
        params=request.GET,
    ).text

    return json.loads(vote)


def get_vote(request, id_):
    vote = requests.get(
        f"http://localhost:8000/api/v1/votes/{id_}/",
        params=request.GET,
    ).text

    return json.loads(vote)


def create_vote(request, id_):
    vote = {"user_id": id_, "vote" : request.POST["vote_name"]}
    requests.post(f"http://localhost:8000/api/v1/votes/", data=vote)