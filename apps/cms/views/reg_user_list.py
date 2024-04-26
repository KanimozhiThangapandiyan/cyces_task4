from rest_framework import generics
from apps.common.models import PersonalDetails
from apps.cms.serializers import UsersSerializer,SingleUserSerializer

class RegisteredUsersListView(generics.ListAPIView):
    #queryset = PersonalDetails.objects.all()
    serializer_class = UsersSerializer

    def get_queryset(self):
        queryset = PersonalDetails.objects.all().prefetch_related(
            'educationandcertifications_set',
            'workdetails_set',
            'employmenthistory_set',
            'awards_set',
            'preferences_set'
        )
        return queryset
    
from django.views import View
from django.http import JsonResponse
from django.http import Http404

class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = SingleUserSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = PersonalDetails.objects.filter(id=user_id)
        if not queryset.exists():
            raise Http404("User does not exist")
        return queryset