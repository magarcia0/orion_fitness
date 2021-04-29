from django import forms
from nutrition.models import NutritionEntry

TASKS_CHOICES= [
    ('-------', '-------'),
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack'),
    ('Other', 'Other'),
]

class NutritionEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category  = forms.CharField(widget=forms.Select(choices=TASKS_CHOICES)) 
	calories = forms.IntegerField()
	calories_goal = forms.IntegerField()
	protein = forms.IntegerField(required=False)
	fats = forms.IntegerField(required=False)
	carbs = forms.IntegerField(required=False)
	class Meta():
		model = NutritionEntry
		fields = ('description', 'category', 'calories', 'calories_goal', 'protein', 'fats', 'carbs')