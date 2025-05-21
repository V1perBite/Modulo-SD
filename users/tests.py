from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User

class UsuarioLoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@example.com", password="test12345")
        self.login_url = reverse('login')

    def test_usuario_login_successful(self):
        response = self.client.post(self.login_url, {'email': 'test@example.com', 'password': 'test12345'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensaje', response.data)

    def test_usuario_login_wrong_credentials(self):
        response = self.client.post(self.login_url, {'email': 'test@example.com', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('non_field_errors', response.data)

    def test_usuario_login_missing_fields(self):
        response = self.client.post(self.login_url, {'email': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)

        self.assertIn('password', response.data)