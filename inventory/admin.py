from django.contrib import admin
from inventory.models import Inputs,Log_association,Log_defect,Log_entrance,Places



# Register your models here.
@admin.register(Inputs)
class InputAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','description','code','amount')
    search_fields =('create','active','update','description','code','amount')

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
