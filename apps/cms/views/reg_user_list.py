from rest_framework.views import APIView
from apps.common.models import PersonalDetails
from apps.cms.serializers import UserDetailsSerializer
from apps.common.response_utils import success_response

class UserDetailsAPIView(APIView):
    def get(self, request, pk):
        personal_details = PersonalDetails.objects.get(pk=pk)
        serializer = UserDetailsSerializer(personal_details)
        return success_response(data=serializer.data)

from rest_framework.generics import ListAPIView
from apps.common.models import PersonalDetails
from apps.cms.serializers import AllUsersDetailsSerializer

class AllUsersDetailsAPIView(ListAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = AllUsersDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)
