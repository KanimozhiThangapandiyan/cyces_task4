from rest_framework import viewsets
from apps.common.models import Industries
from apps.common.serializers import IndustriesSerializer

class IndustriesViewSet(viewsets.ModelViewSet):
    queryset = Industries.objects.all()
    serializer_class = IndustriesSerializer