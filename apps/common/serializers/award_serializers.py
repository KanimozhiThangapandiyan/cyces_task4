from rest_framework import serializers
from apps.common.models import Awards

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields =['award_name','awarding_organization']