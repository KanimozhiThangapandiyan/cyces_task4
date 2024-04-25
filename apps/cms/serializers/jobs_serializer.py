from rest_framework import serializers
from apps.cms.models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'company_name', 'location', 'skills', 'industry', 'vacancy']

class JobPostingSerializerListing(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'company_name', 'location', 'skills', 'industry', 'vacancy','posted_on']
