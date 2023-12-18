from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def homeApi(request):
    return render(request, 'home_api.html')