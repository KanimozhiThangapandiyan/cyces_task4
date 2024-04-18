from rest_framework import serializers
from apps.common.models import Certifications

class CerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = ['certification_name','year_of_certification']