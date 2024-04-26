from rest_framework import serializers

#countrylist
from apps.common.models import Country
class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields ='__all__'

#satelist
from apps.common.models import State
class StateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

#degreelist
from apps.common.models import Degree
class DegreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields ='__all__'

#skills list
from apps.common.models import Skills
class SkillsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

#industrieslist
from apps.common.models import Industries
class IndustriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'

#salary expectation list
from apps.common.models import SalaryExpectation
class SalaryExpectationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryExpectation
        fields = '__all__'