from django.shortcuts import render
from django.views import generic

from serviciu.models import Serviciu


# Create your views here.
class IndexServiciiView(generic.ListView):
    template_name = 'serviciu/index.html'
    context_object_name = "servicii"

    def get_queryset(self):
        return Serviciu.objects.all()