from django.shortcuts import render
from django.http import HttpResponse
from . models import RegisterUsers

# Create your views here.
def register(request):
    return render(request, 'RegisterApp/index.html')



