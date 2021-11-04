from django.contrib import admin
from .models import Report_human_resources,Dashbaners,Calendar
# Register your models here.
@admin.register(Report_human_resources)
class Report_human_resourcesAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','file','file_name',)
    search_fields =('id','create','active','file','file_name',)


@admin.register(Dashbaners)
class DashbanersAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','image','desc','manager',)
    search_fields =('id','create','active','image','desc','manager',)    

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('create','active','reserve','location')
    search_fields = ('create','active','reserve','location')