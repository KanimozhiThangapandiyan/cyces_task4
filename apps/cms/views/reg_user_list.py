from rest_framework import generics
from apps.common.models import PersonalDetails
from apps.cms.serializers import UsersSerializer

class RegisteredUsersListView(generics.ListAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = UsersSerializer
