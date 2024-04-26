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

from django.http import Http404
from rest_framework import generics
from apps.common.models import PersonalDetails, EducationAndCertifications, WorkDetails, EmploymentHistory, Awards, Preferences

class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = SingleUserSerializer

    def get_object(self):
        personal_details_id = self.kwargs.get('id')

        try:
            # Retrieve personal details object
            personal_details = PersonalDetails.objects.get(id=personal_details_id)
        except PersonalDetails.DoesNotExist:
            raise Http404("User does not exist")

        # Retrieve related data
        education_certifications = EducationAndCertifications.objects.filter(user_id=personal_details)
        work_details = WorkDetails.objects.filter(user_id=personal_details)
        employment_history = EmploymentHistory.objects.filter(user_id=personal_details)
        awards = Awards.objects.filter(user_id=personal_details)
        preferences = Preferences.objects.filter(user_id=personal_details)

        # Construct user details dictionary
        user_details = {
            'id': personal_details.id,
            'first_name': personal_details.first_name,
            'last_name': personal_details.last_name,
            'phone_number': personal_details.phone_number,
            'email_id': personal_details.email_id,
            'address': personal_details.address,
            'country': personal_details.country,
            'state': personal_details.state,
            'city': personal_details.city,
            'education_and_certifications': education_certifications,
            'work_details': work_details,
            'employment_history': employment_history,
            'awards': awards,
            'preferences': preferences
        }

        return user_details
