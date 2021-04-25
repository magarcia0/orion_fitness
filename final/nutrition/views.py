from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from nutrition.models import NutritionEntry
from nutrition.forms import NutritionEntryForm
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.


@login_required(login_url='/login/')
def nutrition(request):
	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		NutritionEntry.objects.filter(id=id).delete()
		return redirect("/nutrition/")
	if (request.method == "GET" and "switch" in request.GET):
		table_data = NutritionEntry.objects.filter(user=request.user)
		nutrition = NutritionEntry.objects.filter(user=request.user)
		res = nutrition.aggregate(sum = Sum('calories'))['sum']
		switch = request.GET["switch"]
		context = {
		"table_data": table_data,
		"switch": switch,
		"res": res,
		}
		return render(request, 'nutrition/nutrition.html', context)
	else:
		table_data = NutritionEntry.objects.filter(user=request.user)
		nutrition = NutritionEntry.objects.filter(user=request.user)
		res = nutrition.aggregate(sum = Sum('calories'))['sum']
		context = {
		"table_data": table_data,
		"res": res,
		}
		return render(request, 'nutrition/nutrition.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			add_form = NutritionEntryForm(request.POST)
			if (add_form.is_valid()):
				description = add_form.cleaned_data["description"]
				category = add_form.cleaned_data["category"]
				calories = add_form.cleaned_data["calories"]
				protein = add_form.cleaned_data["protein"]
				fats = add_form.cleaned_data["fats"]
				carbs = add_form.cleaned_data["carbs"]
				user = User.objects.get(id=request.user.id)
				NutritionEntry(user = user, description=description, category=category, calories=calories, protein=protein, fats=fats, carbs=carbs).save()
				return redirect("/nutrition/")
			else:
				context = {
				"form_data": add_form
				}
				return render(request, 'nutrition/add.html', context)
		else:
			# Cancel
			return redirect("/nutrition/")
	else:
		context = {
		"form_data": NutritionEntryForm()
		}
		return render(request, 'nutrition/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		nutritionEntry = NutritionEntry.objects.get(id=id)
		form = NutritionEntryForm(instance=nutritionEntry)
		context = { "form_data" : form }
		return render(request, 'nutrition/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = NutritionEntryForm(request.POST)
			if (form.is_valid()):
				nutritionEntry = form.save(commit=False)
				nutritionEntry.user = request.user
				nutritionEntry.id = id
				nutritionEntry.save()
				return redirect("/nutrition/")
			else:
				context = {
				"form_data": form
				}
				return render(request, 'nutrition/add.html', context)
		else:
			#Cancel
			return redirect("/nutrition/")

def toggle(request, id):
	if (request.method == "GET" and "toggle_completed" in request.GET):
		id = request.GET["toggle_completed"]
		nutrition = Nutrition.object.get(id=id)
		nutrition.completed = not nutrition.completed 
		nutritionEntry.save()
	return redirect("/nutrition/")

def pie_chart(request):
	c_counter = 0
	p_counter = 0
	dataSet = NutritionEntry.objects.filter(user=request.user)
	for x in dataSet:
		if(x.completed == True):
			c_counter = c_counter + 1
		else:
			p_ccounter = p_counter + 1
	return render(request, 'core/home.html/', {
		'c_counter': c_counter,
		'p_counter': p_counter,
	})