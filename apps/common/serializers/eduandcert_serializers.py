from rest_framework import serializers
from apps.common.models import Degree,Certifications,EducationAndCertifications
from .degree_serializers import DegreeSerializer
from .certification_serializer import CertificationSerializer

class EducationAndCertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationAndCertifications
        fields = ['degree','year_of_passing','school','certifications']

    