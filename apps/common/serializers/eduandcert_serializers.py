from rest_framework import serializers
from apps.common.models import Degree,Certifications,EducationAndCertifications
from .degree_serializers import DegreeSerializer
from .certification_serializer import CerificationSerializer

class EducationAndCertificationsSerializer(serializers.ModelSerializer):
    #degree = DegreeSerializer(many=True)
    certifications = CerificationSerializer(many=True) 

    class Meta:
        model = EducationAndCertifications
        fields = ['degree','year_of_passing','school','certifications']

    # def create(self, validated_data):
    #     certifications_data = validated_data.pop('certifications', None)
    #     education_instance = EducationAndCertifications.objects.create(**validated_data)
        
    #     if certifications_data:
    #         for certification_data in certifications_data:
    #             certification_instance = Certifications.objects.create(**certification_data)
    #             education_instance.certifications.add(certification_instance)

    #     return education_instance