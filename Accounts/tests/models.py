from django.test import TestCase

from django.contrib.auth.models import User

from Accounts.models import Account, Cart


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Accounts models test:")
        cls.testuser = User.objects.create_user(username='testuser', password='12345')
        cls.testaccount = Account.objects.create(user=cls.testuser)
        cls.testcart = Cart.objects.create(user=cls.testuser)

    def test_account_model_str(self):
        self.assertEqual(str(self.testaccount), 'testuser')