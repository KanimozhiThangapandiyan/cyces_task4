from django.contrib import admin
from apps.common.models import Country,State,PersonalDetails,Certifications,\
    Degree,EducationAndCertifications,Skills,WorkDetails,EmploymentHistory,Awards,\
        Industries,SalaryExpectation,Preferences

admin.site.register(Country)
admin.site.register(State)
admin.site.register(PersonalDetails)
admin.site.register(Degree)
admin.site.register(Certifications)
admin.site.register(EducationAndCertifications)
admin.site.register(Skills)
admin.site.register(WorkDetails)
admin.site.register(EmploymentHistory)
admin.site.register(Awards)
admin.site.register(Industries)
admin.site.register(SalaryExpectation)
admin.site.register(Preferences)

