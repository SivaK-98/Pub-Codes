from django.shortcuts import render
from .models import Pet
from django.shortcuts import render
from django.http import HttpResponse, Http404




def home(request):
    pet_details = Pet.objects.all()
    return render(request, 'home.html', {'pet_details': pet_details})

def details(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404("PET does not exist")
    return render(request, 'details.html', {'pet': pet})