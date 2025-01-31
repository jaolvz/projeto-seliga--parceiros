from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required(login_url='cadastro:inicio')
def pag_inicial(request):
    return render(request,'pag_inicial.html')