from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TASKS_CHOICES= [
    ('-------', '-------'),
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
    ('Other', 'Other'),
]

class NutritionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=TASKS_CHOICES)
    calories = models.IntegerField()
    protein = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    switcharoo = models.BooleanField(default=False)