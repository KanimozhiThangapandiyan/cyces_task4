from rest_framework import serializers
from apps.common.models import SalaryExpectation

class SalaryExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryExpectation
        fields = ['salary_range']