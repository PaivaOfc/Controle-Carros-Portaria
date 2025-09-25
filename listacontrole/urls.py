from django.urls import path
from . import views

app_name = 'listacontrole'

urlpatterns = [
    path('', views.listHome, name='home'),
]
