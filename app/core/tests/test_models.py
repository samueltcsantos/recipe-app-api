from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@otunac.com'
        password = "otunac#123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user(self):
        """ Test the email for new user is normalized """
        email = "test@OTUNAC.COM"
        user = get_user_model().objects.create_user(email, 'password#123')
        self.assertEqual(user.email, email.lower())


