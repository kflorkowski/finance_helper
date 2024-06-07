from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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


class BudgetPlan(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MonthlyBudget(models.Model):
    budget_plan = models.ForeignKey(BudgetPlan, on_delete=models.CASCADE, related_name="monthly_budget")
    date = models.DateField()  # mm/rrrr
    start_amount = models.DecimalField(max_digits=15, decimal_places=2)
    end_amount = models.DecimalField(max_digits=15, decimal_places=2)
    people = models.ManyToManyField(Person, related_name='budgets')

    def __str__(self):
        return f"{self.budget_plan.name} - {self.date.strftime('%Y-%m')}"

    class Meta:
        unique_together = ('budget_plan', 'date')


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    category_name = models.CharField(max_length=128)

    def __str__(self):
        return self.category_name

    class Meta:
        unique_together = ('user', 'category_name')


class Expense(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.title} - {self.amount}"
