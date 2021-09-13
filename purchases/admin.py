from django.contrib import admin

# Register your models here.
from .models import Purchase_requisition,Requisition_product



# Register your models here.
@admin.register(Purchase_requisition)
class Purchase_requisitionAdmin(admin.ModelAdmin):
    list_display = ('create','active','changed','purchase_requisition_id','requester','manager',)
    search_fields =('create','active','changed','purchase_requisition_id','requester','manager',)
@admin.register(Requisition_product)
class Requisition_productAdmin(admin.ModelAdmin):
    list_display = ('create','active','changed','id','purchase_requisition_id','requisition_product','price_product','amount',)
    search_fields =('create','active','changed','id','purchase_requisition_id','requisition_product','price_product','amount',)
