from django.test import TestCase
from .models import Usuarios
from datetime import date

class UsuariosModelTest(TestCase):
    
    def setUp(self):
        self.usuario = Usuarios.objects.create(
            first_name="Juan",
            last_name="Pérez",
            birth_date=date(1995, 5, 20),
            gender="M",
            email="juan.perez@example.com",
            phone_number="3123456789",
            address="Calle 123, Ciudad"
        )

    def test_usuario_str(self):
        self.assertEqual(str(self.usuario), "Juan Pérez")

    def test_usuario_email_unique(self):
        with self.assertRaises(Exception):  # IntegrityError o ValidationError según el caso
            Usuarios.objects.create(
                first_name="Otro",
                last_name="Usuario",
                birth_date=date(1990, 1, 1),
                gender="M",
                email="juan.perez@example.com",  # Duplicado
            )

    def test_usuario_optional_fields(self):
        user = Usuarios.objects.create(
            first_name="Ana",
            last_name="Gómez",
            birth_date=date(2000, 10, 10),
            gender="F",
            email="ana.gomez@example.com"
        )
        self.assertIsNone(user.phone_number)
        self.assertIsNone(user.address)

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.usuario.created_at)
