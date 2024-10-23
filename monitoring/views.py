from rest_framework import viewsets
from .serializer import MonitoringSerializer
from .models import Monitoring

class MonitoringView(viewsets.ModelViewSet):
    serializer_class = MonitoringSerializer
    queryset = Monitoring.objects.all()
