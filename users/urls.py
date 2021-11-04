from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .api.api import perfil_view,user_view,user_by_idView,create_user_view,office_view,general_Banner_view,create_banner_view,modify_banner_view
from .api.api import manager_Banner_view,user_birth,export_view,user_notes_view,users_view,all_general_Banner_view,all_manager_Banner_view,create_office_view
from . import views

from rest_framework import routers, urlpatterns
router = routers.DefaultRouter()


router.register('users',users_view,'users')
router.register('user',user_view,'user')
# router.register('cargo',office_view,'cargo')
router.register('profile',perfil_view,'profile')
router.register('banners',general_Banner_view,'banners')
router.register('all_banners',all_general_Banner_view,'all_banners')
router.register('manage_banners',manager_Banner_view,'manage_banners')
router.register('all_manage_banners',all_manager_Banner_view,'all_manage_banners')
router.register('aniversarios_mes',user_birth,'aniversarios_mes ')


urlpatterns = [   
    path('exportar/',export_view.as_view(),name="exportar"),
    path('cadastrar/',create_user_view.as_view(),name="cadastrar"),
    path('criar_banner/',create_banner_view.as_view(),name="criar_banner"),
    path('desativar_banner/',modify_banner_view.as_view(),name="desativar_banner"),
    path('notes/<int:code>/',user_notes_view.as_view(),name="notes"),
    path('usuario_por_id/<int:pk>',user_by_idView.as_view(),name="usuario_por_id"),
    path('criar_cargo',create_office_view.as_view(),name="criar_cargo"),
    path('cargo',office_view.as_view(),name="cargo"),
 
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += router.urls