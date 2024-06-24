from django.shortcuts import render
from django.contrib import messages
from . forms import CrewForm
from . models import Job, Crew

# Create your views here.

def crew_main(request):
    crews = Crew.objects.all()
    context = {
        'crews' : crews
    }
    return render(request, 'crew_main.html', context)
