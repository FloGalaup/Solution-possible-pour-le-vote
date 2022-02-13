from .views import (
    UserViewSet,
    AssetViewSet,
    WalletViewSet,
    PostingViewSet,
    ReservationViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register("users", UserViewSet, basename="user")
router.register("wallets", WalletViewSet, basename="wallet")
router.register("assets", AssetViewSet, basename="asset")
router.register("postings", PostingViewSet, basename="posting")
router.register("reservations", ReservationViewSet, basename="reservations")

urlpatterns = router.urls