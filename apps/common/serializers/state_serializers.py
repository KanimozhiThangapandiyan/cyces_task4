from rest_framework import serializers
from apps.common.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
