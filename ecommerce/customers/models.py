from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .choice import GENDER_CHOICE


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=120, unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)

    def __str__(self):
        return self.name
