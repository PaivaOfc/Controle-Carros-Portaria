from django.shortcuts import render

# Create your views here.

def listHome(request):
    return render(request, 'listacontrole/home.html')