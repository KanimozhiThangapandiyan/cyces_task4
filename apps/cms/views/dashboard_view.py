from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.cms.models import JobPosting
from apps.common.models import PersonalDetails

class DashBoardListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        job_posting_count = JobPosting.objects.count()
        personal_details_count = PersonalDetails.objects.count()
        data = {
            'job_posting_count': job_posting_count,
            'Appliations': personal_details_count
        }
        return Response(data, status=status.HTTP_200_OK)