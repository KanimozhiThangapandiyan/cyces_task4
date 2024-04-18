from django.db import models
from .base import Base
from django.core.validators import RegexValidator

class Country(Base):
    country_name = models.CharField(max_length=25, default='India')

    def __str__(self):
        return self.country_name
    
class State(Base):
    state_name = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.state_name}, {self.country.country_name}"

class PersonalDetails(Base):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, unique=True, validators=[RegexValidator(regex=r'^(\+91)?[0-9]{10}$', 
                                message='Phone number must be 10 digits with optional +91 prefix.')])
    email_id = models.EmailField(unique=True)
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
