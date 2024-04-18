from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,StateViewSet,DegreeViewSet,IndustriesViewSet,\
    SalaryExpectationViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'degrees', DegreeViewSet)
router.register(r'industries', IndustriesViewSet)
router.register(r'salary-expectation', SalaryExpectationViewSet)

urlpatterns = []+router.urls