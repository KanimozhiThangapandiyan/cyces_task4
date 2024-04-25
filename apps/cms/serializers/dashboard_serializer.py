from rest_framework import serializers
from apps.cms.models import DashBoard

class DashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashBoard
        fields = '__all__'

