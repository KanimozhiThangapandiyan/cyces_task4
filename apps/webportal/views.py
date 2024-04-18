
from rest_framework import viewsets
from apps.common.serializers import PersonalDetailsSerializer
from apps.common.models import PersonalDetails

class PersonalDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

