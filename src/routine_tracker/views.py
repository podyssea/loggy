from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Workout



def workout_details_page(request, slug):
    # queryset = Workout.objects.filter(slug=slug)
    #
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()

    obj = get_object_or_404(Workout, slug=slug)
    template_name = 'workout_details.html'
    context = {"object": obj}
    return render(request, template_name, context)