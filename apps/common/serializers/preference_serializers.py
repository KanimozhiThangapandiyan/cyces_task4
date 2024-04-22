from rest_framework import serializers
from apps.common.models import Preferences
from .country_serializers import CountrySerializer
from .industries_serialisers import IndustriesSerializer
from .salary_expec_serializers import SalaryExpectationSerializer

class PreferencesSerializer(serializers.ModelSerializer):
    #country = CountrySerializer()
    #industries = IndustriesSerializer()
    #salary_expectations = SalaryExpectationSerializer()

    class Meta:
        model = Preferences
        fields = ['country','industries','position','available_from','salary_expectations']
    