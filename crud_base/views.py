from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def criar_usuario(request):
    # return HttpResponse("<h1> Alô Senai Games!</h'>")
    # request - requisição 
    # template - html entre outros
    # context - objetos (python, python com bd) 
   
   
   
    return render(request, 'crud_base/usuario_lead.html')
