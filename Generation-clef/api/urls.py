from .views import (
    UserViewSet,
    WalletViewSet,
    VoteViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register("users", UserViewSet, basename="user")
router.register("wallets", WalletViewSet, basename="wallet")
router.register("votes", VoteViewSet, basename="vote")

urlpatterns = router.urls
