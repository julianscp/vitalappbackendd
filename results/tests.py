from django.test import TestCase
from datetime import date
from core.models import Usuarios
from results.models import Result

class ResultModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuarios.objects.create(
            first_name="María",
            last_name="López",
            birth_date=date(1992, 6, 5),
            gender="F",
            email="maria.lopez@example.com"
        )
        self.resultado = Result.objects.create(
            patient=self.usuario,
            test_name="Glucosa en sangre",
            result_value="120 mg/dL",
            date=date(2025, 4, 30)
        )

    def test_result_creation(self):
        self.assertEqual(Result.objects.count(), 1)
        self.assertEqual(self.resultado.patient, self.usuario)
        self.assertEqual(self.resultado.test_name, "Glucosa en sangre")
        self.assertEqual(self.resultado.result_value, "120 mg/dL")
        self.assertEqual(self.resultado.date, date(2025, 4, 30))

    def test_result_str_representation(self):
        expected_str = f"Glucosa en sangre de María López - 2025-04-30"
        self.assertEqual(str(self.resultado), expected_str)

    def test_user_result_reverse_relation(self):
        resultados = self.usuario.result.all()
        self.assertIn(self.resultado, resultados)

    def test_delete_user_cascades_result(self):
        self.usuario.delete()
        self.assertEqual(Result.objects.count(), 0)
