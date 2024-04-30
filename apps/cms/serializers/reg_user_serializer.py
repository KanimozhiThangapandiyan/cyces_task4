from rest_framework import serializers
from apps.common.models import PersonalDetails,EducationAndCertifications,WorkDetails,EmploymentHistory,Awards,Preferences
class UserDetailsSerializer(serializers.ModelSerializer):
    education_and_certifications = serializers.SerializerMethodField()
    preferences = serializers.SerializerMethodField()
    employment_history = serializers.SerializerMethodField()
    awards = serializers.SerializerMethodField()
    work_details = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = PersonalDetails
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email_id', 'address', 'country', 'state', 'city', 'education_and_certifications', 'preferences', 'employment_history', 'awards', 'work_details']

    def get_country(self, obj):
        return obj.country.country_name if obj.country else None

    def get_state(self, obj):
        return obj.state.state_name if obj.state else None

    def get_education_and_certifications(self, obj):
        education_certifications = EducationAndCertifications.objects.filter(user_id=obj)
        return [{'degree': [degree.name for degree in education.degree.all()],
                 'year_of_passing': education.year_of_passing,
                 'school': education.school,
                 'certifications': [{'certification_name': cert.certification_name,
                                      'year_of_certification': cert.year_of_certification}
                                     for cert in education.certifications.all()]}
                for education in education_certifications]

    def get_work_details(self, obj):
        work_details = WorkDetails.objects.filter(user_id=obj)
        return [{'skills': [skill.skill_name for skill in work.skills.all()],
                 'total_experience': work.total_experience}
                for work in work_details]

    def get_employment_history(self, obj):
        employment_history = EmploymentHistory.objects.filter(user_id=obj)
        return [{'job_title': history.job_title,
                 'employer': history.employer,
                 'country': history.country.country_name if history.country else None,
                 'state': history.state.state_name if history.state else None,
                 'city': history.city,
                 'from_date': history.from_date,
                 'to_date': history.to_date}
                for history in employment_history]

    def get_awards(self, obj):
        awards = Awards.objects.filter(user_id=obj)
        return [{'award_name': award.award_name,
                 'awarding_organization': award.awarding_organization}
                for award in awards]

    def get_preferences(self, obj):
        preferences = Preferences.objects.filter(user_id=obj)
        return [{'country': preference.country.country_name if preference.country else None,
                 'industries': preference.industries.field if preference.industries else None,
                 'position': preference.position,
                 'available_from': preference.available_from,
                 'salary_expectations': preference.salary_expectations.salary_range if preference.salary_expectations else None}
                for preference in preferences]




class AllUsersDetailsSerializer(serializers.ModelSerializer):
    education_and_certifications = serializers.SerializerMethodField()
    preferences = serializers.SerializerMethodField()
    employment_history = serializers.SerializerMethodField()
    awards = serializers.SerializerMethodField()
    work_details = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()

    class Meta:
        model = PersonalDetails
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email_id', 'address', 'country', 'state', 'city', 'education_and_certifications', 'preferences', 'employment_history', 'awards', 'work_details']

    def get_country(self, obj):
        return obj.country.country_name if obj.country else None

    def get_state(self, obj):
        return obj.state.state_name if obj.state else None

    def get_education_and_certifications(self, obj):
        education_certifications = EducationAndCertifications.objects.filter(user_id=obj)
        return [{'degree': [degree.name for degree in education.degree.all()],
                 'year_of_passing': education.year_of_passing,
                 'school': education.school,
                 'certifications': [{'certification_name': cert.certification_name,
                                      'year_of_certification': cert.year_of_certification}
                                     for cert in education.certifications.all()]}
                for education in education_certifications]

    def get_work_details(self, obj):
        work_details = WorkDetails.objects.filter(user_id=obj)
        return [{'skills': [skill.skill_name for skill in work.skills.all()],
                 'total_experience': work.total_experience}
                for work in work_details]

    def get_employment_history(self, obj):
        employment_history = EmploymentHistory.objects.filter(user_id=obj)
        return [{'job_title': history.job_title,
                 'employer': history.employer,
                 'country': history.country.country_name if history.country else None,
                 'state': history.state.state_name if history.state else None,
                 'city': history.city,
                 'from_date': history.from_date,
                 'to_date': history.to_date}
                for history in employment_history]

    def get_awards(self, obj):
        awards = Awards.objects.filter(user_id=obj)
        return [{'award_name': award.award_name,
                 'awarding_organization': award.awarding_organization}
                for award in awards]

    def get_preferences(self, obj):
        preferences = Preferences.objects.filter(user_id=obj)
        return [{'country': preference.country.country_name if preference.country else None,
                 'industries': preference.industries.field if preference.industries else None,
                 'position': preference.position,
                 'available_from': preference.available_from,
                 'salary_expectations': preference.salary_expectations.salary_range if preference.salary_expectations else None}
                for preference in preferences]



