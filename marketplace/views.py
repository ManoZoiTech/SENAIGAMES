from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    # return HttpResponse("<h1> Alô Senai Games!</h'>")
    # request - requisição 
    # template - html entre outros
    # context - objetos (python, python com bd) 
   
   

    return render(request, 'marketplace/index.html')
        
def autenticar_membro(request):
    dados = {
        1: {"nome":"Visual Novel"},
        2: {"nome":"Plataforma"},
        3: {"nome":"Acao"}
        
    }
    return render(request, 'marketplace/sou_membro.html', {'cards': dados})
