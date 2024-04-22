from rest_framework import serializers
from apps.common.models import PersonalDetails,Certifications,Skills,EducationAndCertifications,WorkDetails,EmploymentHistory,Awards,Preferences
from .country_serializers import CountrySerializer
from .state_serializers import StateSerializer
from .eduandcert_serializers import EducationAndCertificationsSerializer
from .work_detail_serializers import WorkDetailsSerializer
from .employment_hist_serializers import EmploymentHistorySerializer
from .award_serializers import AwardsSerializer
from .preference_serializers import PreferencesSerializer
from django.http import response
from apps.common.models import Country,State


class PersonalDetailsSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()
    education_and_certifications = EducationAndCertificationsSerializer()#
    work_details = WorkDetailsSerializer()#
    employment_history = EmploymentHistorySerializer()#
    awards = AwardsSerializer()#
    preferences = PreferencesSerializer()

    class Meta:
        model = PersonalDetails
        # fields = ['first_name','last_name','phone_number','email_id','address','country','state','city','education_and_certifications','work_details','employment_history','awards','preferences']
        fields='__all__'
        depth=2

    def create(self, validated_data):
        country_data = validated_data.pop('country', None)
        state_data = validated_data.pop('state', None)
        education_and_certifications_data = validated_data.pop('education_and_certifications', {})
        work_details_data = validated_data.pop('work_details', {})
        employment_history_data = validated_data.pop('employment_history', {})
        awards_data = validated_data.pop('awards', {})
        preferences_data = validated_data.pop('preferences', {})

        # Handle country
        if country_data:
            country_instance, _ = Country.objects.get_or_create(id=country_data.get('id'))
            validated_data['country'] = country_instance

        # Handle state
        if state_data:
            state_id = state_data.pop('id', None)
            country_id = state_data.pop('country', None)
            if state_id:
                country_instance = Country.objects.get(id=country_id)
                state_instance, _ = State.objects.get_or_create(id=state_id, country=country_instance)
                validated_data['state'] = state_instance

        personal_details = PersonalDetails.objects.create(**validated_data)

        # Handle nested serializers
        education_and_certifications_serializer = EducationAndCertificationsSerializer(data=education_and_certifications_data)
        if education_and_certifications_serializer.is_valid():
            education_and_certifications_serializer.save(personal_details=personal_details)

        work_details_serializer = WorkDetailsSerializer(data=work_details_data)
        if work_details_serializer.is_valid():
            work_details_serializer.save(personal_details=personal_details)

        employment_history_serializer = EmploymentHistorySerializer(data=employment_history_data)
        if employment_history_serializer.is_valid():
            employment_history_serializer.save(personal_details=personal_details)

        awards_serializer = AwardsSerializer(data=awards_data)
        if awards_serializer.is_valid():
            awards_serializer.save(personal_details=personal_details)

        preferences_serializer = PreferencesSerializer(data=preferences_data)
        if preferences_serializer.is_valid():
            preferences_serializer.save(personal_details=personal_details)

        return personal_details
