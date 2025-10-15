from django.shortcuts import render

from rest_framework import viewsets
from .models import Usuarios
from .serializers import CoreSerializer


class CoreViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = CoreSerializer
