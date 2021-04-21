from django import forms
from nutrition.models import NutritionEntry

TASKS_CHOICES= [
    ('Home', 'Home'),
    ('School', 'School'),
    ('Work', 'Work'),
    ('Self Imporvement', 'Self Improvement'),
    ('Other', 'Other'),
]

class NutritionEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category  = forms.CharField(widget=forms.Select(choices=TASKS_CHOICES)) 
	class Meta():
		model = NutritionEntry
		fields = ('description', 'category')