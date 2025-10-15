from django.test import TestCase
from core.models import Usuarios
from alerts.models import Alert
from datetime import date

class AlertModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuarios.objects.create(
            first_name="Carlos",
            last_name="Ramírez",
            birth_date=date(1988, 3, 22),
            gender="M",
            email="carlos.ramirez@example.com"
        )
        self.alert = Alert.objects.create(
            patient=self.usuario,
            message="Se detectó un valor anormal en su presión arterial.",
            is_read=False
        )

    def test_alert_creation(self):
        self.assertEqual(Alert.objects.count(), 1)
        self.assertEqual(self.alert.patient, self.usuario)
        self.assertEqual(self.alert.message, "Se detectó un valor anormal en su presión arterial.")
        self.assertFalse(self.alert.is_read)
        self.assertIsNotNone(self.alert.created_at)

    def test_alert_str_representation(self):
        expected = "Alerta para Carlos Ramírez - No leída"
        self.assertEqual(str(self.alert), expected)

    def test_alert_read_status_change(self):
        self.alert.is_read = True
        self.alert.save()
        self.alert.refresh_from_db()
        self.assertTrue(self.alert.is_read)

    def test_user_alerts_reverse_relation(self):
        alerts = self.usuario.alerts.all()
        self.assertIn(self.alert, alerts)

    def test_alert_deleted_with_user(self):
        self.usuario.delete()
        self.assertEqual(Alert.objects.count(), 0)
