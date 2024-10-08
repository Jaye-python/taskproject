# tests.py
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase


class CustomUserModelTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_email_unique(self):
        with self.assertRaises(IntegrityError):
            self.user_model.objects.create_user(
                email="testuser@example.com", password="testpassword2"
            )

    def test_default_ordering(self):
        user1 = self.user_model.objects.create_user(
            email="testuser1@example.com", password="testpassword"
        )
        user2 = self.user_model.objects.create_user(
            email="testuser2@example.com", password="testpassword"
        )
        users = self.user_model.objects.all()
        self.assertEqual(users[0], user2)
        self.assertEqual(users[1], user1)

    def test_user_creation_without_username(self):
        user = self.user_model.objects.create_user(
            email="newuser@example.com", password="newpassword"
        )
        self.assertIsNone(user.username)

    def test_user_creation_with_missing_email(self):
        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(email="", password="testpassword")

    def test_user_manager_create_superuser(self):
        superuser = self.user_model.objects.create_superuser(
            email="admin@example.com", password="adminpassword"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
