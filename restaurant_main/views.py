from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'restaurant_main/index.html') # Render main page index.html.