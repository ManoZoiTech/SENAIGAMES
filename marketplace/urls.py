# urls exclusivas do aplicativo crud_base
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('membro/',views.autenticar_membro,name='membro')
]