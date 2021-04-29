from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from workout.models import WorkoutEntry
from workout.forms import WorkoutEntryForm
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.

@login_required(login_url='/login/')
def workout(request):
	db_actual = []
	db_projected = []
	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		WorkoutEntry.objects.filter(id=id).delete()
		return redirect("/workout/")
	else:
		table_data = WorkoutEntry.objects.filter(user=request.user)
		workout = WorkoutEntry.objects.filter(user=request.user)
		for x in table_data:
			x.res = x.actual - x.projected
			db_actual.append(str(x.actual))
			db_projected.append(str(x.projected))
		context = {
		"table_data": table_data,
		"db_actual": db_actual,
		"db_projected": db_projected,
		}
		return render(request, 'workout/workout.html', context)

@login_required(login_url='/login/')
def add(request):
	if (request.method == "POST"):
		if ("add" in request.POST):
			add_form = WorkoutEntryForm(request.POST)
			if (add_form.is_valid()):
				exercise = add_form.cleaned_data["exercise"]
				category = add_form.cleaned_data["category"]
				projected = add_form.cleaned_data["projected"]
				actual = add_form.cleaned_data["actual"]
				user = User.objects.get(id=request.user.id)
				WorkoutEntry(user = user, exercise=exercise, category=category, projected=projected, actual=actual).save()
				return redirect("/workout/")
			else:
				context = {
				"form_data": add_form
				}
				return render(request, 'workout/add.html', context)
		else:
			# Cancel
			return redirect("/workout/")
	else:
		context = {
		"form_data": WorkoutEntryForm()
		}
		return render(request, 'workout/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Journal Entry Form with current model data.
		workoutEntry = WorkoutEntry.objects.get(id=id)
		form = WorkoutEntryForm(instance=workoutEntry)
		context = { "form_data" : form }
		return render(request, 'workout/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = WorkoutEntryForm(request.POST)
			if (form.is_valid()):
				workoutEntry = form.save(commit=False)
				workoutEntry.user = request.user
				workoutEntry.id = id
				workoutEntry.save()
				return redirect("/workout/")
			else:
				context = {
				"form_data": form
				}
				return render(request, 'workout/add.html', context)
		else:
			#Cancel
			return redirect("/workout/")
