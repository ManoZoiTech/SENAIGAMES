from django.db import models

# Aqui eu vou programar o modelo
# Classes mapeadas com tabelas
# Persistência?
# Orientação a objetos
# classes -> tabelas
# localhost:8000/site/admin
# github

# herança 
class Membro(models.Model):
    email = models.CharField(max_length=50,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)
    nome = models.CharField(max_length=80,null=False,blank=False)

    def __self__ (self):
        return f"Nome [nome={self.nome}]"

 