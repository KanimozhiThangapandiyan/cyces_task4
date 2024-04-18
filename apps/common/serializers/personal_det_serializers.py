from rest_framework import serializers
from apps.common.models import PersonalDetails
from .country_serializers import CountrySerializer
from .state_serializers import StateSerializer
from .eduandcert_serializers import EducationAndCertificationsSerializer
from .work_detail_serializers import WorkDetailsSerializer
from .employment_hist_serializers import EmploymentHistorySerializer
from .award_serializers import AwardsSerializer
from .preference_serializers import PreferencesSerializer

class PersonalDetailsSerializer(serializers.ModelSerializer):
    #country = CountrySerializer()
    #state = StateSerializer()
    education_and_certifications = EducationAndCertificationsSerializer()#
    work_details = WorkDetailsSerializer()#
    employment_history = EmploymentHistorySerializer()#
    #awards = AwardsSerializer()#
    preferences = PreferencesSerializer()

    class Meta:
        model = PersonalDetails
        fields = ['first_name','last_name','phone_number','email_id','address','country','state','city','education_and_certifications','work_details','employment_history','preferences']