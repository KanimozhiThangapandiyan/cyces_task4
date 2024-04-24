from django.db import models
from .base import Base
from django.core.validators import MinValueValidator, MaxValueValidator
from .personal_details import Country,State,PersonalDetails

class Skills(Base):
    skill_name = models.CharField(max_length=15)

    def __str__(self):
        return self.skill_name
    
class WorkDetails(models.Model):
    user_id=models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,default=11)
    skills = models.ManyToManyField(Skills)
    total_experience = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(15)]
    )

    def __str__(self):
        return f"Work Details: {self.total_experience} years"
    
class EmploymentHistory(models.Model):
    user_id=models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,default=11)
    job_title = models.CharField(max_length=20)
    employer = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f"{self.job_title} at {self.employer}"
    
class Awards(models.Model):
    user_id=models.ForeignKey(PersonalDetails, on_delete=models.CASCADE,default=11)
    award_name = models.CharField(max_length=25)
    awarding_organization = models.CharField(max_length=30)

    def __str__(self):
        return self.award_name

