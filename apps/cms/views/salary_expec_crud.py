from rest_framework import viewsets
from apps.common.models import SalaryExpectation
from apps.common.serializers import SalaryExpectationSerializer

class SalaryExpectationViewSet(viewsets.ModelViewSet):
    queryset = SalaryExpectation.objects.all()
    serializer_class = SalaryExpectationSerializer