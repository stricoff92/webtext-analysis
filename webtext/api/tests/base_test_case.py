
from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from django.contrib.auth.models import User

from .factory import TestObjectFactory

class BaseTestBase(TestCase):
    PASSWORD_FACTORY = "super-secure-password-yo"
    ADMIN_USER_NAME = "foobarius-admin"
    USER_NAME = "foobarina-user"
    OTHER_USER_NAME = "foobarathan-user"

    factory = TestObjectFactory()


    def setUp(self):
        self.client = TestClient()

        self.user = User.objects.create_user(
            username=self.USER_NAME,
            email=f'{self.USER_NAME}@mail.com',
            password=self.PASSWORD_FACTORY)

        self.other_user = User.objects.create_user(
            username=self.OTHER_USER_NAME,
            email=f'{self.OTHER_USER_NAME}@mail.com',
            password=self.PASSWORD_FACTORY)

    def tearDown(self):
        self.client.logout()
