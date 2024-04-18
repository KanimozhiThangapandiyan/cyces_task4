from rest_framework import serializers
from apps.common.models import EmploymentHistory
from .country_serializers import CountrySerializer
from .state_serializers import StateSerializer
from .award_serializers import AwardsSerializer

class EmploymentHistorySerializer(serializers.ModelSerializer):
    #country = CountrySerializer() 
    #state = StateSerializer()
    awards=AwardsSerializer(many=True)

    class Meta:
        model = EmploymentHistory
        fields = ['job_title','employer','country','state','city','from_date','to_date','awards']