from rest_framework import serializers
from apps.common.models import Country,State,PersonalDetails
# from apps.common.models import PersonalDetails,Certifications,Skills,EducationAndCertifications,WorkDetails,EmploymentHistory,Awards,Preferences
# from .country_serializers import CountrySerializer
# from .state_serializers import StateSerializer
# from .eduandcert_serializers import EducationAndCertificationsSerializer
# from .work_detail_serializers import WorkDetailsSerializer
# from .employment_hist_serializers import EmploymentHistorySerializer
# from .award_serializers import AwardsSerializer
# from .preference_serializers import PreferencesSerializer
# from django.http import response


class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields=['first_name','last_name','phone_number','email_id','address','country','state','city']
        

