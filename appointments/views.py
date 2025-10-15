from rest_framework import viewsets
from .models import Appointments
from .serializers import AppointmentsSerializer


class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
