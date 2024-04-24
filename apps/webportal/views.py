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
        education_certifications_serializer = EducationAndCertificationsSerializer(data=education_certifications_data)
        work_details_serializer = WorkDetailsSerializer(data=work_details_data)
        employment_history_serializer = EmploymentHistorySerializer(data=employment_history_data)
        awards_serializer = AwardsSerializer(data=awards_data)
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
            
            if 'skills' in work_details_data:
                work_details_instance.skills.set(work_details_data['skills'])
            
            if 'certifications' in education_certifications_data:
                certifications_data = education_certifications_data.pop('certifications')
                for certification_data in certifications_data:
                    certification_serializer = CertificationSerializer(data=certification_data)
                    if certification_serializer.is_valid():
                        certification_instance = certification_serializer.save()
                        education_certifications_instance.certifications.add(certification_instance)
                    else:
                        return Response(
                            {
                                'error': certification_serializer.errors
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
            
            return Response(
                {
                    'personal_details': personal_details_instance.data,
                    'education_and_certifications': education_certifications_instance.data,
                    'work_details': work_details_instance.data,
                    'employment_history': employment_history_instance.data,
                    'awards': awards_instance.data,
                    'preferences': preferences_instance.data,
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


# from rest_framework.generics import CreateAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from apps.common.models import Certifications
# from apps.common.serializers import (PersonalDetailsSerializer, 
#                           EducationAndCertificationsSerializer,
#                           WorkDetailsSerializer,
#                           EmploymentHistorySerializer,
#                           AwardsSerializer,
#                           CertificationSerializer,
#                           PreferencesSerializer)

# class SaveDataView(APIView):
#     def post(self, request, *args, **kwargs):
#         personal_details_data = request.data.get('personal_details')
#         #print(personal_details_data)
#         education_certifications_data = request.data.get('education_and_certifications')
#         #print(education_certifications_data)
#         work_details_data = request.data.get('work_details')
#         #print(work_details_data)
#         employment_history_data = request.data.get('employment_history')
#         #print(employment_history_data)
#         awards_data = request.data.get('awards')
#         #print(awards_data)
#         preferences_data = request.data.get('preferences')
#         #print(preferences_data)
        
#         personal_details_serializer = PersonalDetailsSerializer(data=personal_details_data)
#         education_certifications_serializer = EducationAndCertificationsSerializer(data=education_certifications_data)
#         work_details_serializer = WorkDetailsSerializer(data=work_details_data)
#         employment_history_serializer = EmploymentHistorySerializer(data=employment_history_data)
#         awards_serializer = AwardsSerializer(data=awards_data)
#         preferences_serializer = PreferencesSerializer(data=preferences_data)
        
#         # Check if all serializers are valid before proceeding
#         serializers_valid = all([
#             personal_details_serializer.is_valid(),
#             education_certifications_serializer.is_valid(),
#             work_details_serializer.is_valid(),
#             employment_history_serializer.is_valid(),
#             awards_serializer.is_valid(),
#             preferences_serializer.is_valid()
#         ])
        
#         if serializers_valid:
#             # Proceed with saving data
#             personal_details_instance = personal_details_serializer.save()
#             education_certifications_instance = education_certifications_serializer.save()
#             work_details_instance = work_details_serializer.save()
#             employment_history_instance = employment_history_serializer.save()
#             awards_instance = awards_serializer.save()
#             preferences_instance = preferences_serializer.save()
            
#             # Handling ManyToMany relationships
#             if 'skills' in work_details_data:
#                 work_details_instance.skills.set(work_details_data['skills'])
            
#             if 'certifications' in education_certifications_data:
#                 certifications_data = education_certifications_data.pop('certifications')
#                 for certification_data in certifications_data:
#                     certification_serializer = CertificationSerializer(data=certification_data)
#                     if certification_serializer.is_valid():
#                         certification_instance = certification_serializer.save()
#                         education_certifications_instance.certifications.add(certification_instance)
#                     else:
#                         return Response(
#                             {
#                                 'error': certification_serializer.errors
#                             },
#                             status=status.HTTP_400_BAD_REQUEST
#                         )
            
#             return Response(
#                 {
#                     'personal_details': personal_details_instance.data,
#                     'education_certifications': education_certifications_instance.data,
#                     'work_details': work_details_instance.data,
#                     'employment_history': employment_history_instance.data,
#                     'awards': awards_instance.data,
#                     'preferences': preferences_instance.data,
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         else:
#             # Return errors if any serializer is invalid
#             return Response(
#                 {
#                     'error': {
#                         'personal_details': personal_details_serializer.errors,
#                         'education_certifications': education_certifications_serializer.errors,
#                         'work_details': work_details_serializer.errors,
#                         'employment_history': employment_history_serializer.errors,
#                         'awards': awards_serializer.errors,
#                         'preferences': preferences_serializer.errors,
#                     }
#                 },
#                 status=status.HTTP_400_BAD_REQUEST
#             )

  

# from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from apps.common.serializers import PersonalDetailsSerializer
# from apps.common.models import PersonalDetails, Country,State

# class PersonalDetailsCreateAPIView(CreateAPIView):
#     serializer_class = PersonalDetailsSerializer
#     queryset = PersonalDetails.objects.all()

#     def create(self, request, *args, **kwargs):
#         data = request.data
#         print(data)
#         country = Country.objects.get(id=data['country'])
#         state = State.objects.get(id=data['state'])
#         personal_detail = PersonalDetails.objects.create(
#             first_name = data['first_name'],
#             last_name = data['last_name'],
#             phone_number=data['phone_number'],
#             email_id=data['email_id'],
#             address=data['address'],
#             city=data['city'],
#             country=country,
#             state=state
#         )
#         personal_detail.save()

#         serializer = PersonalDetailsSerializer(personal_detail)
#         return Response(serializer.data)
