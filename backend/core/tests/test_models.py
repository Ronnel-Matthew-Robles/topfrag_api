from django.test import TestCase
# from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_create_user_str(self):
        """Test the user string representation"""
        username = 'test'
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = models.User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        self.assertEqual(str(user), f'@{username}')
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
