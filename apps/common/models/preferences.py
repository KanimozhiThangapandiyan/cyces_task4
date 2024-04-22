from django.db import models
from .personal_details import Country
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
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default=1)
    industries = models.ForeignKey(Industries, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    available_from = models.DateField()

    salary_expectations = models.ForeignKey(SalaryExpectation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Preferences: {self.position} in {self.country} for {self.industries}"
