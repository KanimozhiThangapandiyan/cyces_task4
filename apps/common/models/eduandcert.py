from django.db import models
from .base import Base

class Degree(Base):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name
    
class Certifications(models.Model):
    certification_name = models.CharField(max_length=35)
    year_of_certification = models.PositiveIntegerField()

    def __str__(self):
        return self.certification_name

class EducationAndCertifications(models.Model):
    degree = models.ManyToManyField(Degree)
    year_of_passing = models.PositiveIntegerField()
    school = models.CharField(max_length=40)
    certifications = models.ManyToManyField(Certifications)


    def __str__(self):
        return f"{self.degree} from {self.school}"
