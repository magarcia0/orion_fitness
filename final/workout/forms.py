from django import forms
from workout.models import WorkoutEntry

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

class WorkoutEntryForm(forms.ModelForm):
	exercise = forms.CharField(label='Description', widget=forms.TextInput(attrs={'size': '80'}))
	category  = forms.CharField(widget=forms.Select(choices=WORKOUT_CHOICES)) 
	projected = forms.DecimalField(label='Projected Time')
	actual = forms.DecimalField(label='Actual Time')
	class Meta():
		model = WorkoutEntry
		fields = ('exercise', 'category', 'projected', 'actual')