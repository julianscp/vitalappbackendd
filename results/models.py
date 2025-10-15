# results/models.py

from django.db import models
from core.models import Usuarios  # Importa tu modelo Core

class Result(models.Model):
    patient = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name="result")
    test_name = models.CharField(max_length=100)
    result_value = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.test_name} de {self.patient} - {self.date}"
