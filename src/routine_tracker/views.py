from django.shortcuts import render

# Create your views here.
from .models import Workout



def workout_details_page(request, workout_id):
    obj = Workout.objects.get(id=workout_id)
    template_name = 'workout_details.html'
    context = {"object": obj}
    return render(request, template_name, context)