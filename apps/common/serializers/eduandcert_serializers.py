from rest_framework import serializers
from apps.common.models import Degree,Certifications,EducationAndCertifications
from .degree_serializers import DegreeSerializer
from .certification_serializer import CertificationSerializer

class EducationAndCertificationsSerializer(serializers.ModelSerializer):
    certifications=CertificationSerializer(many=True)
    class Meta:
        model = EducationAndCertifications
        fields = ['degree','year_of_passing','school','certifications']

        def create(self, validated_data):
            certifications_data = validated_data.pop('certifications')
            education_and_certifications = EducationAndCertifications.objects.create(**validated_data)
            
            for certification_data in certifications_data:
                Certifications.objects.create(education_and_certifications=education_and_certifications, **certification_data)
            
            return education_and_certifications
        