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


class Job(models.Model):
    CONTRACT_CHOICES = (
        ('UOM', 'Umowa o prace'),
    )
    company = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    gross_salary = models.DecimalField(max_digits=15, decimal_places=2)
    contract = models.CharField(max_length=3, choices=CONTRACT_CHOICES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='jobs')
