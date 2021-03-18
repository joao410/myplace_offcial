from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [   
    path('rh_chamado',views.rh_chamado, name="rh_chamado"),
    path('chamado/add_chamado',views.add_chamado, name="add_chamado"),
    path('chamado/dash_index',views.dash_index, name="dash_index"),
    path('chamado/tecnicos',views.tecnico, name="tecnicos"),
    path('chamado/<int:id>',views.id_chamado, name="id_chamado"),
    path('chamado/dash_index/<int:id>',views.atendimento,  name="atendimento"),
    path('chamado/chat/<int:id>',views.chat,  name="chat"),
    path('chamado/linksup',views.linksup, name="linksup"),

 

   
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)