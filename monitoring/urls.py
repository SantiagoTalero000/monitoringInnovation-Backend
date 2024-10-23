from django.urls import include, path
from rest_framework import routers
from monitoring import views

router = routers.DefaultRouter()
router.register(r"monitoring", views.MonitoringView, "monitoring")

urlpatterns = [
    path("api/", include(router.urls))
]