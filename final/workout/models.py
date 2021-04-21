from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BUDGET_CHOICES= [
    ('Food', 'Food'),
    ('Clothing', 'Clothing'),
    ('Housing', 'Housing'),
    ('Education', 'Education'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other'),
    ]

class WorkoutEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=BUDGET_CHOICES)
    projected = models.IntegerField()
    actual = models.IntegerField()