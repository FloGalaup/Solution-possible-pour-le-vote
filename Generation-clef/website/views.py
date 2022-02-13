import json
from django.shortcuts import render
from .services.posting_service import get_postings


def index(request):
    postings = get_postings(request)
    context = {"postings": json.loads(postings)}

    return render(request, "website/index.html", context)


def postings(request):
    context = {}
    return render(request, "website/postings.html", context)


def about(request):
    context = {}
    return render(request, "website/about.html", context)


def contact(request):
    context = {}
    return render(request, "website/contact.html", context)

def connexion(request):
    context = {}
    return render(request, "website/connexion.html", context)
