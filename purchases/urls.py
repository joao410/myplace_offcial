from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .api.api import req_View,req_val_View,req_val_View,purchases_View,purchase_View,req_bou_man_appr_View,req_den_View,req_cot_View,purchases_by_name_View,create_req_View
from .api.api import  fin_appr_View,boug_View,pay_req_View,del_req_by_prod_View,ret_req_View,req_by_id_View,req_prod_by_id_View
from rest_framework import routers, urlpatterns
router = routers.DefaultRouter()

router.register('requisicoes',purchases_View,'requisicoes')
router.register('requisicoes_por_nome',purchases_by_name_View,'requisicoes_por_nome')
urlpatterns = [   
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
    path('req/',req_View.as_view(),name="req"),

 
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
