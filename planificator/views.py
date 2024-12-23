from django.shortcuts import render
from django.views import generic

from planificator.models import Programare


# Create your views here.
class IndexPlanificatorView(generic.ListView):
    template_name = 'planificator/index.html'
    context_object_name = 'planificator'

    def get_queryset(self):
        return Programare.objects.all()