from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
