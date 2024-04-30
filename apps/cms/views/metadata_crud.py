from rest_framework import generics
from rest_framework import viewsets
from apps.common.response_utils import success_response


#crud for country
from apps.common.models import Country
from apps.common.serializers import CountrySerializer
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

#countrylist
from apps.cms.serializers import CountryListSerializer
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)


#crud for state
from apps.common.models import State
from apps.common.serializers import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

#statelist
from apps.cms.serializers import StateListSerializer
class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)


#crud for degree
from apps.common.models import Degree
from apps.common.serializers import DegreeSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

#degreelist
from apps.cms.serializers import DegreeListSerializer
class DegreeListView(generics.ListAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)

#crud for skills
from apps.common.models import Skills
from apps.common.serializers import SkillsSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


#skillslist
from apps.cms.serializers import SkillsListSerializer
class SkillsListView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)

#crud for industries
from apps.common.models import Industries
from apps.common.serializers import IndustriesSerializer
class IndustriesViewSet(viewsets.ModelViewSet):
    queryset = Industries.objects.all()
    serializer_class = IndustriesSerializer

#Industrylist
from apps.cms.serializers import IndustriesListSerializer
class IndustryListView(generics.ListAPIView):
    queryset = Industries.objects.all()
    serializer_class = IndustriesListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)

##crud for salary expectations
from apps.common.models import SalaryExpectation
from apps.common.serializers import SalaryExpectationSerializer
class SalaryExpectationViewSet(viewsets.ModelViewSet):
    queryset = SalaryExpectation.objects.all()
    serializer_class = SalaryExpectationSerializer

#salary expectation list
from apps.cms.serializers import SalaryExpectationListSerializer
class SalaryExpectationsListView(generics.ListAPIView):
    queryset = SalaryExpectation.objects.all()
    serializer_class = SalaryExpectationListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(data=serializer.data)