from rest_framework import serializers
from apps.common.models import Certifications

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'