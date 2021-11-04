from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .api.api import called_view,called_by_group_view,called_by_idView,called_by_name_view ,answer_call_View,end_call_View,reopen_call_View,redirect_call_View,called_grafics_views, create_call_View,maneger_View
from rest_framework import routers, urlpatterns
router = routers.DefaultRouter()
router.register('chamados',called_view,'chamados')
router.register('chamados_por_grupo',called_by_group_view,'chamados_por_grupo')
router.register('chamados_por_nome',called_by_name_view,'chamados_por_nome')
router.register('gestores',maneger_View,'gestores')

urlpatterns = [   
  
    path('fazer_chamado',create_call_View.as_view(),name="fazer_chamado"),
    path('chamado_por_id/<int:id>',called_by_idView.as_view(),name="chamado_por_id"),
    path('atender_chamado/<int:id>',answer_call_View.as_view(),name="atender_chamado"),
    path('encerrar_chamado/<int:id>',end_call_View.as_view(),name="encerrar_chamado"),
    path('reabrir_chamado/<int:id>',reopen_call_View.as_view(),name="reabrir_chamado"),
    path('redirecionar_chamado/<int:id>',redirect_call_View.as_view(),name="redirecionar_chamado"),
    path('graficos/',called_grafics_views.as_view(),name="graficos"),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += router.urls
