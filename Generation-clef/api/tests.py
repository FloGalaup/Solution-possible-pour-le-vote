from urllib import response
from django.test import TestCase
from rest_framework.test import RequestsClient
from .models import User


class UserTestCase(TestCase):
    def setup(self):
        User.objects.create(
            id="1",
            username="test_user",
            email="test@email.com",
            private_key="xyz",
            public_key="abc",
            password="test_password",
        )

        self.client = RequestsClient()

    def test_retrieve_user_should_return_200(self):
        response = self.client.get("http://localhost:8000/api/v1/users/1/")

        assert response.status_code == 200
