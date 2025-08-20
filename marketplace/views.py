from django.shortcuts import render
from django.http import HttpResponse
from marketplace.models import Membro
# Create your views here.
def index(request):

    # return HttpResponse("<h1> Alô Senai Games!</h'>")
    # request - requisição 
    # template - html entre outros
    # context - objetos (python, python com bd) 
   
   

    return render(request, 'marketplace/index.html')
        
def autenticar_membro(request):
    # dados = {
    #     1: {"nome":"Visual Novel"},
    #     2: {"nome":"Plataforma"},
    #     3: {"nome":"Acao"}
        
    # }

    membros = Membro.objects.all()
    return render(request, 'marketplace/sou_membro.html', {'cards': dados})
