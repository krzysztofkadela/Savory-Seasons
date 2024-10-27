from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'restaurant_main/index.html') # Render main page index.html.