from rest_framework import serializers
from apps.common.models import WorkDetails
from .skills_serializers import SkillsSerializer


class WorkDetailsSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True)

    class Meta:
        model = WorkDetails
        fields = ['skills','total_experience']