from datetime import datetime
from .models import User, Wallet, Asset, Posting, Reservation
from .serializers import (
    UserSerializer,
    WalletSerializer,
    AssetSerializer,
    PostingSerializer,
    ReservationSerializer,
)
from .helpers.cryptography import create_hash
from .helpers.utils import calculate_reservation_cost
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all().order_by("id")
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = User()

        user.username = request.data["username"]
        user.email = request.data["email"]
        user.rating = request.data["rating"]
        user.picture_url = request.data["picture_url"]
        user.password = request.data["password"]

        user.save()

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        user.username = request.data["username"]
        user.email = request.data["email"]
        user.rating = request.data["rating"]
        user.picture_url = request.data["picture_url"]
        user.password = request.data["password"]

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["POST"])
    def custom(self, request, pk=None):
        pass


class WalletViewSet(viewsets.ViewSet):
    def list(self, request):
        wallets = Wallet.objects.all().order_by("funds")
        wallets_serializer = WalletSerializer(wallets, many=True)

        return Response(wallets_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        wallet = Wallet()

        pk = request.data["user_id"]
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        wallet.owner = user
        wallet.name = request.data["name"]
        wallet.private_key = "xyz"  #! Create Private Key
        wallet.public_key = "xyz"  #! Create Public Key
        wallet.funds = 0

        wallet.save()

        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Wallet.objects.all()
        wallet = get_object_or_404(queryset, pk=pk)

        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Wallet.objects.all()
        wallet = get_object_or_404(queryset, pk=pk)

        wallet.name = request.data["name"]

        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Wallet.objects.all()
        wallet = get_object_or_404(queryset, pk=pk)

        wallet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["PATCH"])
    def add_funds(self, request, pk=None):
        pass

    @action(detail=True, methods=["POST"])
    def send_funds(self, request, pk=None):
        pass


class AssetViewSet(viewsets.ViewSet):
    def list(self, request):
        assets = Asset.objects.all().order_by("name")
        assets_serializer = AssetSerializer(assets, many=True)

        return Response(assets_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        asset = Asset()

        pk = request.data["user_id"]
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        asset.owner = user
        asset.name = request.data["name"]
        asset.description = request.data["description"]
        asset.image_url = request.data["image_url"]
        asset.rating = request.data["rating"]

        asset.save()

        asset_serializer = AssetSerializer(asset)

        return Response(asset_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Asset.objects.all()
        asset = get_object_or_404(queryset, pk=pk)

        asset_serializer = AssetSerializer(asset)

        return Response(asset_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Asset.objects.all()
        asset = get_object_or_404(queryset, pk=pk)

        asset.name = request.data["name"]
        asset.description = request.data["description"]
        asset.image_url = request.data["image_url"]
        asset.rating = request.data["rating"]

        asset_serializer = AssetSerializer(asset)

        return Response(asset_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Asset.objects.all()
        asset = get_object_or_404(queryset, pk=pk)

        asset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["POST"])
    def custom(self, request, pk=None):
        pass


class PostingViewSet(viewsets.ViewSet):
    def list(self, request):
        postings = Posting.objects.all().order_by("title")
        postings_serializer = PostingSerializer(postings, many=True)

        return Response(postings_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        posting = Posting()

        pk = request.data["asset_id"]
        queryset = Asset.objects.all()
        asset = get_object_or_404(queryset, pk=pk)

        posting.asset = asset
        posting.title = request.data["title"]
        posting.description = request.data["description"]
        posting.available = request.data["available"]

        date_posted = datetime.now()
        posting.date_posted = date_posted
        posting.last_modified = date_posted

        posting.starting_date = request.data["starting_date"]
        posting.end_date = request.data["end_date"]
        posting.cost_per_day = request.data["cost_per_day"]

        posting.save()

        posting_serializer = PostingSerializer(posting)

        return Response(posting_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Posting.objects.all()
        posting = get_object_or_404(queryset, pk=pk)

        posting_serializer = PostingSerializer(posting)

        return Response(posting_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Posting.objects.all()
        posting = get_object_or_404(queryset, pk=pk)

        posting.title = request.data["title"]
        posting.description = request.data["description"]
        posting.available = request.data["available"]
        posting.last_modified = datetime.now()
        posting.starting_date = request.data["starting_date"]
        posting.end_date = request.data["end_date"]
        posting.cost_per_day = request.data["cost_per_day"]

        posting_serializer = PostingSerializer(posting)

        return Response(posting_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Posting.objects.all()
        posting = get_object_or_404(queryset, pk=pk)

        posting.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["POST"])
    def custom(self, request, pk=None):
        pass


class ReservationViewSet(viewsets.ViewSet):
    def list(self, request):
        reservations = Reservation.objects.all().order_by("starting_date")
        reservations_serializer = ReservationSerializer(reservations, many=True)

        return Response(reservations_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        reservation = Reservation()

        posting_pk = request.data["posting_id"]
        posting_queryset = Posting.objects.all()
        posting = get_object_or_404(posting_queryset, pk=posting_pk)

        user_pk = request.data["user_id"]
        user_queryset = User.objects.all()
        user = get_object_or_404(user_queryset, pk=user_pk)

        reservation.posting = posting
        reservation.user = user
        reservation.starting_date = request.data["starting_date"]
        reservation.end_date = request.data["end_date"]
        reservation.date_booked = datetime.now()
        reservation.total_cost = calculate_reservation_cost(posting)

        reservation.save()

        reservation_serializer = ReservationSerializer(reservation)

        return Response(reservation_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Reservation.objects.all()
        reservation = get_object_or_404(queryset, pk=pk)

        reservation_serializer = ReservationSerializer(reservation)

        return Response(reservation_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Reservation.objects.all()
        reservation = get_object_or_404(queryset, pk=pk)

        posting_pk = request.data["posting_id"]
        posting_queryset = Posting.objects.all()
        posting = get_object_or_404(posting_queryset, pk=posting_pk)

        user_pk = request.data["user_id"]
        user_queryset = User.objects.all()
        user = get_object_or_404(user_queryset, pk=user_pk)

        reservation.posting = posting
        reservation.user = user
        reservation.starting_date = request.data["starting_date"]
        reservation.end_date = request.data["end_date"]
        reservation.last_modified = datetime.now()
        reservation.total_cost = calculate_reservation_cost(posting)

        reservation_serializer = ReservationSerializer(reservation)

        return Response(reservation_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Reservation.objects.all()
        reservation = get_object_or_404(queryset, pk=pk)

        reservation.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["POST"])
    def custom(self, request, pk=None):
        pass
