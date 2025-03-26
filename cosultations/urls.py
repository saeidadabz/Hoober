from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultationSessionViewSet

router = DefaultRouter()
router.register(r"sessions", ConsultationSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("sessions/<int:pk>/reserve/", ConsultationSessionViewSet.as_view({"patch": "reserve"}), name="reserve-session"),
]