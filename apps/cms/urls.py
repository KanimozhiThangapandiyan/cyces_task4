from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,StateViewSet,DegreeViewSet,IndustriesViewSet,\
    SalaryExpectationViewSet,JobPostingListCreateView,JobPostingRetrieveUpdateDeleteView,ChangePasswordAPIView,DashBoardListView

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'degrees', DegreeViewSet)
router.register(r'industries', IndustriesViewSet)
router.register(r'salary-expectation', SalaryExpectationViewSet)

urlpatterns = [
    path('job-postings/', JobPostingListCreateView.as_view(), name='job-posting-list-create'),
    path('job-postings/<int:pk>/', JobPostingRetrieveUpdateDeleteView.as_view(), name='job-posting-retrieve-update-delete'),
    path('password-change/', ChangePasswordAPIView.as_view(), name='password_change'),
    path('dashboard/', DashBoardListView.as_view(), name='dashboard_list'),


] + router.urls