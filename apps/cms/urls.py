from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet,StateViewSet,DegreeViewSet,IndustriesViewSet,SkillsViewSet,SkillsListView,\
    SalaryExpectationViewSet,CountryListView,StateListView,DegreeListView,IndustryListView,SalaryExpectationsListView,\
        JobPostingListCreateView,JobPostingRetrieveUpdateDeleteView,ChangePasswordAPIView,\
        DashBoardListView,UserDetailsAPIView,AllUsersDetailsAPIView,ExportUserDataAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
#


router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'degrees', DegreeViewSet)
router.register(r'industries', IndustriesViewSet)
router.register(r'salary-expectation', SalaryExpectationViewSet)
router.register(r'skills',SkillsViewSet)

urlpatterns = [
    path('country-list/', CountryListView.as_view(), name='country-list'),
    path('state-list/', StateListView.as_view(), name='state-list'),
    path('degree-list/', DegreeListView.as_view(), name='degree-list'),
    path('industry-list/',IndustryListView.as_view(), name='industry-list'),
    path('sal-expec-list/', SalaryExpectationsListView.as_view(), name='salary-expec-list'),
    path('skills-list/', SkillsListView.as_view(), name='skills-list'),
    path('job-postings/', JobPostingListCreateView.as_view(), name='job-posting-list-create'),
    path('job-postings/<int:pk>/', JobPostingRetrieveUpdateDeleteView.as_view(), name='job-posting-retrieve-update-delete'),
    path('password-change/', ChangePasswordAPIView.as_view(), name='password_change'),
    path('dashboard/', DashBoardListView.as_view(), name='dashboard_list'),
    path('user/<int:pk>/', UserDetailsAPIView.as_view(), name='user-data-list'),
    path('registered-users/',AllUsersDetailsAPIView.as_view(), name='registered-users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-export/<int:user_id>/', ExportUserDataAPIView.as_view(), name='export-user-data'),

]+router.urls
