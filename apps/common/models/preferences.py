from django.db import models
from .personal_details import Country,PersonalDetails
from .base import Base


class Industries(Base):
    field = models.CharField(max_length=20)

    def __str__(self):
        return self.field
    
class SalaryExpectation(Base):
    salary_range = models.CharField(max_length=20)


    def __str__(self):
        return self.salary_range
    
class Preferences(models.Model):
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='preferences',on_delete=models.SET_DEFAULT)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default=1)
    industries = models.ForeignKey(Industries, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    available_from = models.DateField()

    salary_expectations = models.ForeignKey(SalaryExpectation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Preferences: {self.position} in {self.country} for {self.industries}"
