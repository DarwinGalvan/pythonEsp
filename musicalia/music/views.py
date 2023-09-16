from django.shortcuts import render
from .models import Cancion

def cancion_list(request):
    cancion_qs = Cancion.objects.all()
    context = {'cancion_qs':cancion_qs}
    return render(request, 'musicalia/vista.html', context)

# Create your views here.
