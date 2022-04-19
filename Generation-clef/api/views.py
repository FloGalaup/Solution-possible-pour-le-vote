from datetime import datetime
from .models import User, Wallet, Vote
from .serializers import (
    UserSerializer,
    WalletSerializer,
    VoteSerializer,
)
from .helpers.cryptography import create_hash
from .helpers.utils import calculate_reservation_cost
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from Crypto.PublicKey import RSA
import datetime
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all().order_by("id")
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = User()

        user.username = request.data["username"]
        user.email = request.data["email"]
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
        user.password = request.data["password"]

        user.save()

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"], url_path="login/(?P<username>\w+)")
    def login(self, request, username):
        user = get_object_or_404(User, username=username)

        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)


class WalletViewSet(viewsets.ViewSet):
    def list(self, request):
        wallets = Wallet.objects.all().order_by("id")
        wallets_serializer = WalletSerializer(wallets, many=True)

        return Response(wallets_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        wallet = Wallet()

        pk = request.data["user_id"]
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        key = RSA.generate(2048)
        clef_prive=key.export_key().decode("utf-8")
        clef_publique=key.publickey().export_key().decode("utf-8")
        wallet.private_key = str(clef_prive).replace("\n","")  #! Create Private Key
        wallet.public_key = str(clef_publique).replace("\n","")  #! Create Public Key

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

        wallet.save()

        wallet_serializer = WalletSerializer(wallet)

        return Response(wallet_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Wallet.objects.all()
        wallet = get_object_or_404(queryset, pk=pk)

        wallet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class VoteViewSet(viewsets.ViewSet):
    def list(self, request):
        votes = Vote.objects.all().order_by("id")
        votes_serializer = VoteSerializer(votes, many=True)

        return Response(votes_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        vote = Vote()

        timestamp=datetime.datetime.now().timestamp()
        timestamp=(str(timestamp)).encode('ascii')
        vote.timestamp = timestamp.decode("utf-8")
        vote.vote = request.data["vote"]
        key = RSA.generate(2048)
        clef_prive=key.export_key().decode("utf-8")
        clef_publique=key.publickey().export_key().decode("utf-8")
        vote.private_key = str(clef_prive).replace("\n","")  #! Create Private Key
        vote.public_key = str(clef_publique).replace("\n","")  #! Create Public Key
        h = SHA256.new((vote.vote).encode("utf-8"))
        rsa = RSA.importKey(clef_prive)
        signer = PKCS1_v1_5.new(rsa)
        signature = signer.sign(h)
        vote.hash = signature

        #hash clé publique
        rsa2 = RSA.importKey(clef_publique)
        signer2 = PKCS1_v1_5.new(rsa2)
        rsp = "Success" if (signer2.verify(h, signature)) else " Verification Failure"
        vote.hash_publique = rsp

        vote.save()

        vote_serializer = VoteSerializer(vote)

        return Response(vote_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Vote.objects.all()
        vote = get_object_or_404(queryset, pk=pk)

        vote_serializer = VoteSerializer(vote)

        return Response(vote_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Vote.objects.all()
        vote = get_object_or_404(queryset, pk=pk)

        vote.timestamp = request.data["timestamp"]
        vote.vote = request.data["vote"]
        vote.hash = request.data["hash"]

        vote.save()

        vote_serializer = WalletSerializer(vote)

        return Response(vote_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Vote.objects.all()
        vote = get_object_or_404(queryset, pk=pk)

        vote.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
