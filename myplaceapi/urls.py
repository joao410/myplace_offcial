from os import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import  performance_view, req_View, req_val_View,called_view,called_by_group_view,called_by_idView,req_val_View,purchases_View,purchase_View,req_bou_man_appr_View,users_view
from .views import called_by_name_view ,answer_call_View,end_call_View,reopen_call_View,redirect_call_View,req_den_View,req_cot_View,purchases_by_name_View
from .views import fin_appr_View,boug_View,pay_req_View,del_req_by_prod_View,ret_req_View,create_call_View,create_req_View,maneger_View,req_by_id_View,req_prod_by_id_View
from users.views import perfil_view,user_view,user_by_idView,create_user_view,office_view,general_Banner_view,create_banner_view,modify_banner_view,manager_Banner_view,user_birth
from inventory.views import product_input_view,product_patrimony_view,product_sales_view
from rest_framework import routers, urlpatterns
from files.views import Report_view,Reports_views

router = routers.DefaultRouter()

router.register('gestores',maneger_View,'gestores')
router.register('performance',performance_view,'performance')
router.register('user',user_view,'user')
router.register('users',users_view,'users')
router.register('profile',perfil_view,'profile')
router.register('chamados',called_view,'chamados')
router.register('chamados_por_grupo',called_by_group_view,'chamados_por_grupo')
router.register('chamados_por_nome',called_by_name_view,'chamados_por_nome')
router.register('requisicoes',purchases_View,'requisicoes')
router.register('requisicoes_por_nome',purchases_by_name_View,'requisicoes_por_nome')
router.register('cargo',office_view,'cargo')
router.register('produtos_patrimonio',product_patrimony_view,'produtos_patrimonio')
router.register('produtos_vendas',product_sales_view,'produtos_vendas')
router.register('produtos_insumos',product_input_view,'produtos_insumos')
router.register('banners',general_Banner_view,'banners')
router.register('manage_banners',manager_Banner_view,'manage_banners')
router.register('aniversarios_mes',user_birth,'aniversarios_mes ')
router.register('all_reports',Reports_views,'all_reports ')








urlpatterns = [
     path('fazer_chamado',create_call_View.as_view(),name="fazer_chamado"),
     path('chamado_por_id/<int:id>',called_by_idView.as_view(),name="chamado_por_id"),
     path('usuario_por_id/<int:pk>',user_by_idView.as_view(),name="usuario_por_id"),
     path('atender_chamado/<int:id>',answer_call_View.as_view(),name="atender_chamado"),
     path('encerrar_chamado/<int:id>',end_call_View.as_view(),name="encerrar_chamado"),
     path('reabrir_chamado/<int:id>',reopen_call_View.as_view(),name="reabrir_chamado"),
     path('redirecionar_chamado/<int:id>',redirect_call_View.as_view(),name="redirecionar_chamado"),
     path('fazer_req',create_req_View.as_view(),name="fazer_req"),
     path('req_por_id/<int:id>',req_by_id_View.as_view(),name="req_por_id"),
     path('prod_req_por_id/<int:id>',req_prod_by_id_View.as_view(),name="prod_req_por_id"),
     path('val_req/<int:id>',req_val_View.as_view(),name="val_req"),
     path('den_req/<int:id>',req_den_View.as_view(),name="den_req"),
     path('cot_req/',req_cot_View.as_view(),name="cot_req"),
     path('gest_com_apr_req/',req_bou_man_appr_View.as_view(),name="gest_com_apr_req"),
     path('apr_fin_req/',fin_appr_View.as_view(),name="apr_fin_req"),
     path('com_req/',boug_View.as_view(),name="com_req"),
     path('pag_req/',pay_req_View.as_view(),name="pag_req"),
     path('ent_pro_req/',del_req_by_prod_View.as_view(),name="ent_pro_req"),
     path('dev_req/',ret_req_View.as_view(),name="dev_req"),
     path('cadastrar/',create_user_view.as_view(),name="cadastrar"),
     path('criar_banner/',create_banner_view.as_view(),name="criar_banner"),
     path('desativar_banner/',modify_banner_view.as_view(),name="desativar_banner"),
     path('reports/',Report_view.as_view(),name="reports"),

   
     path('req/',req_View.as_view(),name="req"),
]



urlpatterns += router.urls


