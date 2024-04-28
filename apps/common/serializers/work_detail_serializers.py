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
        skills_ids = validated_data.pop('skills')  # Remove skills data from validated_data
        work_details = WorkDetails.objects.create(**validated_data)  # Create WorkDetails instance
        
        for skill_id in skills_ids:
            # Fetch the Skill object based on the ID and associate it with the work_details instance
            skill = Skills.objects.get(id=skill_id.id)
            work_details.skills.add(skill)

        # for skill_data in skills_data:
        #     skills_serializer = SkillsSerializer(data=skill_data)
        #     if skills_serializer.is_valid():
        #         skill_instance = skills_serializer.save()
        #         work_details.skills.add(skill_instance)
        #     else:
        #         # Handle serializer errors if necessary
        #         pass

        return work_details