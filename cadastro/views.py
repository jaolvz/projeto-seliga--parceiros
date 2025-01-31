from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def inicio(request):
   return render(request,'inicio.html')

def cadastro(request):
    if request.method == 'POST':

        email  = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirmar = request.POST.get('confirmar_senha')
        
        usuario  =  User.objects.filter(email=email).first()
        if usuario:
            pass # retorno um json response informando que o email já está cadastrad
    
        if confirmar_senha(senha, senha_confirmar): #se passar, eu confirmo a senha
            usuario = User.objects.create_user(username=email, password=senha)
            usuario.save()
            return redirect('cadastro:inicio')
            
    else:
        return render(request,'cadastro.html')
    

def confirmar_senha (senha1, senha2):
    if senha1==senha2:
        return True
    return False
