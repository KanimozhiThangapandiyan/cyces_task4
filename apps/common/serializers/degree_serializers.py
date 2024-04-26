from rest_framework import serializers
from apps.common.models import Degree

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id','name']