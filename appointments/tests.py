from django.test import TestCase
from datetime import datetime
from core.models import Usuarios
from .models import Appointments

class AppointmentsModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuarios.objects.create(
            first_name="Laura",
            last_name="González",
            birth_date="1990-08-15",
            gender="F",
            email="laura.gonzalez@example.com"
        )
        self.appointment = Appointments.objects.create(
            patient=self.usuario,
            date=datetime(2025, 5, 10, 14, 30),
            reason="Consulta general"
        )

    def test_appointment_creation(self):
        self.assertEqual(Appointments.objects.count(), 1)
        self.assertEqual(self.appointment.patient, self.usuario)
        self.assertEqual(self.appointment.reason, "Consulta general")
        self.assertEqual(self.appointment.date, datetime(2025, 5, 10, 14, 30))

    def test_appointment_str(self):
        expected_str = "Cita de Laura González el 2025-05-10 14:30:00"
        self.assertEqual(str(self.appointment), expected_str)

    def test_cascade_delete_usuario(self):
        self.usuario.delete()
        self.assertEqual(Appointments.objects.count(), 0)

    def test_usuario_appointments_reverse_relation(self):
        self.assertIn(self.appointment, self.usuario.appointments.all())
