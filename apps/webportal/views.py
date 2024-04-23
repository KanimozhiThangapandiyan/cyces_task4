
from rest_framework import viewsets
# from apps.common.serializers import PersonalDetailsSerializer
from apps.common.models import PersonalDetails

# class PersonalDetailsViewSet(viewsets.ModelViewSet):
#     

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from apps.common.serializers import (PersonalDetailsSerializer, EducationAndCertificationsSerializer,
                          CertificationSerializer, WorkDetailsSerializer,
                          EmploymentHistorySerializer, AwardsSerializer,
                          PreferencesSerializer)

class PersonalDetailsViewSet(viewsets.ViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

    @action(detail=False, methods=['post'])
    def add_user_register_details(self, request):
        personal_serializer = PersonalDetailsSerializer(data=request.data.get('personal_details'))
        educational_serializer = EducationAndCertificationsSerializer(data=request.data.get('education_and_certifications'))
        work_serializer = WorkDetailsSerializer(data=request.data.get('work_details'))
        employment_history_serializer = EmploymentHistorySerializer(data=request.data.get('employment_history'))
        awards_serializer = AwardsSerializer(data=request.data.get('awards'))
        preference_serializer = PreferencesSerializer(data=request.data.get('preferences'))

        # Validate all serializers
        validation_errors = {}

        serializers_data = {
            'personal_details': personal_serializer,
            'educational_details': educational_serializer,
            'work_details': work_serializer,
            'employment_history': employment_history_serializer,
            'awards_details': awards_serializer,
            'preference_details': preference_serializer,
        }

        for serializer_name, serializer in serializers_data.items():
            if not serializer.is_valid():
                validation_errors[serializer_name] = serializer.errors
        
        if validation_errors:
            return Response({'errors': validation_errors}, status=status.HTTP_400_BAD_REQUEST)

        # Save data using all serializers
        personal_instance = personal_serializer.save()
        educational_instance = educational_serializer.save()
        work_instance = work_serializer.save()
        employment_history_instance = employment_history_serializer.save()
        awards_instance = awards_serializer.save()
        preference_instance = preference_serializer.save()

        # Return success response
        return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)