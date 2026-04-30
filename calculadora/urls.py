from django.urls import path
from . import views

urlpatterns = [
    path('imc/', views.calcular_imc, name='calculadora_imc'),
    path('calc1/', views.pagina1, name='pagina1'),
    path('calc2/', views.pagina2,name = 'teste pagina'),
    path('torradeira/', views.torradeira, name ='torra animada'),
    path('sistema_solar/', views.sistema_solar, name = 'sistema girando')
]
