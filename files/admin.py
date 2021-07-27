from django.contrib import admin
from .models import Report_human_resources
# Register your models here.
@admin.register(Report_human_resources)
class Report_human_resourcesAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','file','file_name',)
    search_fields =('id','create','active','file','file_name',)

