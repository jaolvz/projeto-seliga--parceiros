from django.urls import path
from . import views


app_name = 'cadastro'
urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('cadastro/', views.cadastro, name='cadastro')
]