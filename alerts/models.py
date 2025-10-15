from django.db import models
from core.models import Usuarios  # Asegúrate de importar tu modelo de usuarios personalizado

class Alert(models.Model):
    patient = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name="alerts")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

    def __str__(self):
        return f"Alerta para {self.patient.first_name} {self.patient.last_name} - {'Leída' if self.is_read else 'No leída'}"
