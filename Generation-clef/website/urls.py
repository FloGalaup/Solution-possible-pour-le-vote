from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("<int:user_id>/view_key", views.view_key, name="view_key"),
    path("<int:user_id>/view_key2", views.view_key2, name="view_key2"),
    path("<int:user_id>/add_wallet", views.add_wallet, name="add_wallet"),
    path("<int:user_id>/vote", views.vote, name="vote"),
    path("<int:user_id>/vote2", views.vote2, name="vote2"),
    path("<int:user_id>/add_vote", views.add_vote, name="add_vote"),
]
