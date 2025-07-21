from django.shortcuts import render
from django.http import HttpResponse
from .models import Type

# Create your views here.
def index(request):
    types = Type.objects.all()
    return render(request, 'menu/index.html', {'types': types})