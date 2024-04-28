from rest_framework.views import APIView
from rest_framework.response import Response
from apps.common.models import PersonalDetails
from apps.cms.serializers import UserDetailsSerializer

class UserDetailsAPIView(APIView):
    def get(self, request, pk):
        personal_details = PersonalDetails.objects.get(pk=pk)
        serializer = UserDetailsSerializer(personal_details)
        return Response(serializer.data)

from rest_framework.generics import ListAPIView
from apps.common.models import PersonalDetails
from apps.cms.serializers import AllUsersDetailsSerializer

class AllUsersDetailsAPIView(ListAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = AllUsersDetailsSerializer

