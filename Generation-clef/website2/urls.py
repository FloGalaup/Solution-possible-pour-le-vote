from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("postings", views.postings, name="postings"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("<int:user_id>/view_key", views.view_key, name="view_key"),
    path("<int:user_id>/dashboard", views.dashboard, name="dashboard"),
    path("<int:user_id>/add_wallet", views.add_wallet, name="add_wallet"),
    path(
        "<int:user_id>/<int:asset_id>/create_posting",
        views.create_posting,
        name="create_posting",
    ),
    path(
        "<int:user_id>/add_asset",
        views.add_asset,
        name="add_asset",
    ),
]
