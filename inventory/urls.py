from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .api.api import product_input_view,product_patrimony_view,product_sales_view

from rest_framework import routers, urlpatterns
router = routers.DefaultRouter()
router.register('produtos_patrimonio',product_patrimony_view,'produtos_patrimonio')
router.register('produtos_vendas',product_sales_view,'produtos_vendas')
router.register('produtos_insumos',product_input_view,'produtos_insumos')
urlpatterns = [   
  
 
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += router.urls
