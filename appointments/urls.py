from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentsViewSet

router = DefaultRouter()
router.register(r"", AppointmentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
