from django.urls import path
from . import views

urlpatterns = [
    path('', views.contar_letras, name='contar_letras'),
]