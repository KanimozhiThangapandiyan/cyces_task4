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
        degrees_ids = validated_data.pop('degree')
        print(degrees_ids)
        education_and_certifications = EducationAndCertifications.objects.create(**validated_data)

        for degree_id in degrees_ids:
            degree = Degree.objects.get(id=degree_id.id)
            education_and_certifications.degree.add(degree)

        # for degree_data in degrees_data:
        #     degree_serializer = DegreeSerializer(data=degree_data)
        #     if degree_serializer.is_valid():
        #         degree_instance = degree_serializer.save()
        #         education_and_certifications.degree.add(degree_instance)
        #     else:
        #         # Handle serializer errors if necessary
        #         pass

        for certification_data in certifications_data:
            certification_serializer = CertificationSerializer(data=certification_data)
            if certification_serializer.is_valid():
                certification_instance = certification_serializer.save()
                education_and_certifications.certifications.add(certification_instance)
            else:
                # Handle serializer errors if necessary
                pass

        return education_and_certifications
            