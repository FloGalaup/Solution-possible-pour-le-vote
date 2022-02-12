import requests


def get_postings(request):
    postings = requests.get(
        "http://localhost:8000/api/v1/postings/", params=request.GET
    ).text

    return postings
