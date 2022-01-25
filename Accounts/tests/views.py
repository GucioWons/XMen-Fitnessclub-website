from django.test import TestCase

from django.contrib.auth.models import User

from Accounts.models import Account


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Accounts views test:")
        cls.testuser = User.objects.create_user(username='testuser', password='12345')
        cls.testaccount = Account.objects.create(user=cls.testuser)