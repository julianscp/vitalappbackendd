from django.db import models
from core.models import Usuarios  # Esto está bien si Usuarios está en core.models

class Appointments(models.Model):
    patient = models.ForeignKey(
        Usuarios, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Cita de {self.patient.first_name} {self.patient.last_name} el {self.date}"
