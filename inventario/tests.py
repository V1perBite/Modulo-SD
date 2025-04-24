from django.test import TestCase
from django.urls import reverse

class VistasBasicasTest(TestCase):
    def test_vista_productos(self):
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)

    def test_vista_entradas(self):
        response = self.client.get(reverse('historial_entradas'))
        self.assertEqual(response.status_code, 200)
