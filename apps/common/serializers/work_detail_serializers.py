from rest_framework import serializers
from apps.common.models import Skills
from apps.common.models import WorkDetails
from .skills_serializers import SkillsSerializer


class WorkDetailsSerializer(serializers.ModelSerializer):
    #skills = SkillsSerializer(many=True)

    class Meta:
        model = WorkDetails
        fields = ['skills','total_experience']

    def create(self, validated_data):
        skills_data = validated_data.pop('skills')  # Remove skills data from validated_data
        work_details = WorkDetails.objects.create(**validated_data)  # Create WorkDetails instance
        
        # # Create Skills instances for each skill_data
        # for skill_data in skills_data:
        #     # Create a new Skills instance for each skill_data
        #     skill_instance = Skills.objects.create(**skill_data)
        #     # Add the newly created skill_instance to the many-to-many relationship
        #     work_details.skills.add(skill_instance)

        for skill_data in skills_data:
            skills_serializer = SkillsSerializer(data=skills_data)
            if skills_serializer.is_valid():
                skill_instance = skills_serializer.save()
                work_details.skills.add(skill_instance)
            else:
                # Handle serializer errors if necessary
                pass

        return work_details