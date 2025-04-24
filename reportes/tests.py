from django.test import TestCase
from django.urls import reverse

class ReporteVistaTest(TestCase):
    def test_generar_reporte(self):
        # Test para comprobar que la vista carga correctamente
        response = self.client.get(reverse('vista_reportes'))
        self.assertEqual(response.status_code, 200)

    def test_generar_reporte_post(self):
        # Test para simular la generación de un reporte en POST
        response = self.client.post(reverse('vista_reportes'), {
            'tipo_reporte': 'ventas',
            'fecha_inicio': '2024-01-01',
            'fecha_fin': '2024-12-31',
            'region': 'Norte',
            'producto': 'MacBook',
            'formato': 'excel'
        })
        self.assertEqual(response.status_code, 200)
