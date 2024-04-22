from rest_framework import serializers
from apps.common.models import Industries

class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'