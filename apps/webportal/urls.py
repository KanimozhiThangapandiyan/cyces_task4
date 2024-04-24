from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaveDataViewSet

# router = DefaultRouter()
# router.register(r'register', SaveDataView)

urlpatterns =[
    path('register/', SaveDataViewSet.as_view({'post': 'create'})),
    ]