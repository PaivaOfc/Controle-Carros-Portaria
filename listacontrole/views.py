from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def listHome(request):
    context = {'form': ContactForm()}
    return render(request, 'listacontrole/home.html', context)