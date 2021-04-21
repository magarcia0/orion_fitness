from django import forms
from workout.models import WorkoutEntry

BUDGET_CHOICES= [
    ('Food', 'Food'),
    ('Clothing', 'Clothing'),
    ('Housing', 'Housing'),
    ('Education', 'Education'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other'),
    ]

class WorkoutEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category  = forms.CharField(widget=forms.Select(choices=BUDGET_CHOICES)) 
	projected = forms.IntegerField()
	actual = forms.IntegerField()
	class Meta():
		model = WorkoutEntry
		fields = ('description', 'category', 'projected', 'actual')