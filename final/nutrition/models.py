from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TASKS_CHOICES= [
    ('Home', 'Home'),
    ('School', 'School'),
    ('Work', 'Work'),
    ('Self Imporvement', 'Self Improvement'),
    ('Other', 'Other'),
    ]

class NutritionEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=TASKS_CHOICES)
    completed = models.BooleanField(default=False)
    switcharoo = models.BooleanField(default=False)