from django.db import models

class DashBoard(models.Model):
    model_name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.model_name} Count: {self.count}"
