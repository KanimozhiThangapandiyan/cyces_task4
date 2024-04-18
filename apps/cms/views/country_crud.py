from rest_framework import viewsets
from apps.common.models import Country
from apps.common.serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
