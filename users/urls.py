from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('',views.home, name="home"),   
   path('users/presidente',views.presidente, name="presidente"),
   path('users/problem',views.problem, name="problem"),
   path('users/perfisuser',views.perfisuser, name="perfisuser"),
   path('users/add_usuarios',views.add_usuarios, name="add_usuarios"),
   path('users/perfis',views.perfis, name="perfis"),
   path('users/perfisuser/<int:id>',views.edit_usuarios, name="edit_usuarios"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)