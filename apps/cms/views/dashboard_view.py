from rest_framework import generics
from apps.cms.models import JobPosting
from apps.common.models import PersonalDetails
from apps.common.response_utils import success_response

class DashBoardListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        job_posting_count = JobPosting.objects.count()
        personal_details_count = PersonalDetails.objects.count()
        data = {
            'job_posting_count': job_posting_count,
            'Appliations': personal_details_count
        }
        return success_response(data=data)