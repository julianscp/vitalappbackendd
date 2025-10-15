# results/serializers.py

from rest_framework import serializers
from .models import Result
from core.models import Usuarios

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
