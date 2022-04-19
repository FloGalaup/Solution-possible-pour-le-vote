from .models import Vote, Wallet, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
        )


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "private_key", "public_key")

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("id","timestamp","vote","hash","hash_publique")


