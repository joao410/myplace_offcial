from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [   
    path('',views.index, name="my_purchase_request"),
    path('purchases/add_requsition',views.add_requisition, name="add_requsition"),
    path('purchases/',views.purchase_request, name="purchase_request"),
    path('purchases/manager_requisition',views.manager_requisition, name="manager_requisition"),
    path('purchases/financial_approval',views.financial_approval, name="financial_approval"),
    path('purchases/manager_req_details/<int:purchase_requisition_id>',views.manager_req_details, name="manager_req_details"),
    path('purchases/financial_appr_details/<int:purchase_requisition_id>',views.financial_appr_details, name="financial_appr_details"),
    path('purchases/<int:purchase_requisition_id>',views.requisition_details, name="requisition_details"),
    path('purchases/cotation/<int:purchase_requisition_id>',views.requisition_cotation, name="requisition_cotation"),
   
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)