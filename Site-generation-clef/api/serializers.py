from .models import Wallet, User, Asset, Posting, Reservation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "rating",
            "picture_url",
            "private_key",
            "public_key",
            "password",
        )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "owner", "name", "private_key", "public_key", "funds")


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ("id", "owner", "name", "description", "image_url", "rating")


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = (
            "id",
            "asset",
            "title",
            "description",
            "date_posted",
            "last_modified",
            "starting_date",
            "end_date",
            "cost_per_day",
        )


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "posting",
            "user",
            "starting_date",
            "end_date",
            "date_booked",
            "total_cost",
        )
