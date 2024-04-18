from rest_framework import viewsets
from apps.common.models import Degree
from apps.common.serializers import DegreeSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
