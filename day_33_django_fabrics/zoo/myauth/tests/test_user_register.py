from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myauth.models import UserModel


class UserRegisterTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_reg_data = {
            "username": "john",
            "email": "john@example.com",
            "password1": "johnjohn123",
            "password2": "johnjohn123",
        }
        cls.user_reg_data_invalid_pass = {
            "username": "john",
            "email": "john@example.com",
            "password1": "johnjohn123",
            "password2": "johnjohn1231",
        }

    def test_user_register_success(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertURLEqual(response.url, reverse("animals:list"))
        user: AbstractUser = UserModel.objects.get(
            username=self.user_reg_data["username"]
        )
        self.assertEqual(user.email, self.user_reg_data["email"])

    def test_user_register_exist_error(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "username",
            _("A user with that username already exists."),
        )

    def test_user_register_password_doesnt_match(self):
        response = self.client.post(
            reverse("user-register"),
            data=self.user_reg_data_invalid_pass,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response,
            "form",
            "password2",
            UserCreationForm.error_messages["password_mismatch"],
        )
