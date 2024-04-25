from django.db import models
from datetime import datetime

class JobPosting(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.TextField()
    industry = models.CharField(max_length=100)
    vacancy = models.PositiveIntegerField()
    posted_on = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.company_name} - {self.location}"
