from rest_framework import serializers
from apps.common.models import PersonalDetails
from apps.common.serializers import ( 
                          EducationAndCertificationsSerializer,
                          WorkDetailsSerializer,
                          EmploymentHistorySerializer,
                          AwardsSerializer,
                          PreferencesSerializer)

class UsersSerializer(serializers.ModelSerializer):
    education_and_certifications = EducationAndCertificationsSerializer(many=True, read_only=True)
    work_details = WorkDetailsSerializer(many=True, read_only=True)
    employment_history = EmploymentHistorySerializer(many=True, read_only=True)
    awards = AwardsSerializer(many=True, read_only=True)
    preferences = PreferencesSerializer(many=True, read_only=True)

    class Meta:
        model = PersonalDetails
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email_id', 'address', 'country', 'state', 'city','education_and_certifications',
                  'work_details','employment_history','awards','preferences']
