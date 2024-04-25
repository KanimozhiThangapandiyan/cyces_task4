from rest_framework import generics
from apps.cms.models import DashBoard
from apps.cms.serializers import DashBoardSerializer

class DashBoardListView(generics.ListAPIView):
    queryset = DashBoard.objects.all()
    serializer_class = DashBoardSerializer
