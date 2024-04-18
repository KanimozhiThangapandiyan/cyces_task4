from rest_framework import serializers
from apps.common.models import EducationAndCertifications
from .degree_serializers import DegreeSerializer
from .certification_serializer import CerificationSerializer

class EducationAndCertificationsSerializer(serializers.ModelSerializer):
    #degree = DegreeSerializer(many=True)
    #certifications = CerificationSerializer(many=True) 

    class Meta:
        model = EducationAndCertifications
        fields = ['degree','year_of_passing', 'school', 'certifications'] 
        # def to_representation(self, instance):
        # representation = super().to_representation(instance)
        # # Extracting specific fields from the degree data
        # degree_representation = []
        # for degree_data in representation['degree']:
        #     degree_representation.append({
        #         'name': degree_data['name'],
        #         'year_of_passing': degree_data['year_of_passing']
        #     })
        # representation['degree'] = degree_representation
        # return representation