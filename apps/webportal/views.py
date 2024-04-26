from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.common.models import PersonalDetails, EducationAndCertifications, WorkDetails, EmploymentHistory, Awards, Preferences
from apps.common.serializers import (PersonalDetailsSerializer, 
                          EducationAndCertificationsSerializer,
                          WorkDetailsSerializer,
                          EmploymentHistorySerializer,
                          AwardsSerializer,
                          CertificationSerializer,
                          PreferencesSerializer)

class SaveDataViewSet(ViewSet):
    def create(self, request, *args, **kwargs):
        personal_details_data = request.data.get('personal_details')
        education_certifications_data = request.data.get('education_and_certifications')
        work_details_data = request.data.get('work_details')
        employment_history_data = request.data.get('employment_history')
        awards_data = request.data.get('awards')
        preferences_data = request.data.get('preferences')
        
        personal_details_serializer = PersonalDetailsSerializer(data=personal_details_data)
        education_certifications_serializer = EducationAndCertificationsSerializer(data=education_certifications_data,many=True)
        work_details_serializer = WorkDetailsSerializer(data=work_details_data,many=True)
        employment_history_serializer = EmploymentHistorySerializer(data=employment_history_data,many=True)
        awards_serializer = AwardsSerializer(data=awards_data,many=True)
        preferences_serializer = PreferencesSerializer(data=preferences_data)
        
        serializers_valid = all([
            personal_details_serializer.is_valid(),
            education_certifications_serializer.is_valid(),
            work_details_serializer.is_valid(),
            employment_history_serializer.is_valid(),
            awards_serializer.is_valid(),
            preferences_serializer.is_valid()
        ])
        
        if serializers_valid:
            personal_details_instance = personal_details_serializer.save()
            education_certifications_instance = education_certifications_serializer.save()
            work_details_instance = work_details_serializer.save()
            employment_history_instance = employment_history_serializer.save()
            awards_instance = awards_serializer.save()
            preferences_instance = preferences_serializer.save()
            
            return Response(
                {
                    'personal_details': personal_details_serializer.data,
                    'education_and_certifications': education_certifications_serializer.data,
                    'work_details': work_details_serializer.data,
                    'employment_history': employment_history_serializer.data,
                    'awards': awards_serializer.data,
                    'preferences': preferences_serializer.data,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'error': {
                        'personal_details': personal_details_serializer.errors,
                        'education_and_certifications': education_certifications_serializer.errors,
                        'work_details': work_details_serializer.errors,
                        'employment_history': employment_history_serializer.errors,
                        'awards': awards_serializer.errors,
                        'preferences': preferences_serializer.errors,
                    }
                },
                status=status.HTTP_400_BAD_REQUEST
            )
