from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('pagina3/', views.pagina3,name = 'pagina3')
]
