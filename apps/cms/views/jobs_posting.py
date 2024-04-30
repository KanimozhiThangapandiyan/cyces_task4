from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.cms.models import JobPosting
from apps.cms.serializers import JobPostingSerializer,JobPostingSerializerListing

class JobPostingListCreateView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticated]

class JobPostingRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializerListing
    permission_classes = [IsAuthenticated]
    
