from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalDetailsViewSet

router = DefaultRouter()
router.register(r'register', PersonalDetailsViewSet)

urlpatterns =[]+router.urls