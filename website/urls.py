from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("postings", views.postings, name="postings"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("connexion",views.connexion, name="connexion")
]
