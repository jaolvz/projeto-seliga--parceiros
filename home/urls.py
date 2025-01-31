from django.urls import path
from . import views


app_name = 'feed'
urlpatterns = [
    path('', views.pag_inicial, name='pag_inicial' ),

]