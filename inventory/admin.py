from django.contrib import admin
from inventory.models import Inputs,Log_association,Log_defect,Log_entrance,Places,Log_Movimantation,Manufacturer



# Register your models here.
@admin.register(Inputs)
class InputAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','associate','description','code','destination','amount')
    search_fields =('create','active','update','associate','description','code','destination','amount')

@admin.register(Log_entrance)
class Log_entranceAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','code','entrance_code','creator')
    earch_fieds = ('create','active','update','code','entrance_code','creator')

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','place','company','department')
    earch_fieds = ('create','active','update','place','company','department')

@admin.register(Log_association)
class Log_associationAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','association_code','code','associate')
    earch_fieds =  ('create','active','update','association_code','code','associate')

@admin.register(Log_defect)
class Log_defectAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','defect_code','code','reason','creator')
    earch_fieds = ('create','active','update','defect_code','code','reason','creator')
@admin.register(Log_Movimantation)
class Log_MovimantationAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','modifyer','code','localization','amount')
    earch_fieds =  ('create','active','update','modifyer','code','localization','amount')
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','manufacturer_code','person','cpf_cnpj','telephone1')
    earch_fieds =  ('create','active','update','manufacturer_code','person','cpf_cnpj','telephone1')
