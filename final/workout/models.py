from django.db import models
from django.contrib.auth.models import User

# Create your models here.

WORKOUT_CHOICES = [
    ('-------', '-------'),
    ('Cardio', 'Cardio'),
    ('Cross-fit', 'Cross-fit'),
    ('Free Weights', 'Free Weights'),
    ('Lower-Body', 'Lower-Body'),
    ('Upper-Body', 'Upper-Body'),
    ('Yoga', 'Yoga'),
    ('Other', 'Other'),
]
class WorkoutEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=128)
    category = models.CharField(max_length=128, choices=WORKOUT_CHOICES)
    projected = models.DecimalField(decimal_places=1, max_digits=99)
    actual = models.DecimalField(decimal_places=1, max_digits=99)
    res = models.DecimalField(default=0.0, decimal_places=1, max_digits=99)
    date = models.DateField(auto_now=True)
