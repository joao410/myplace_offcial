from django.contrib import admin
from .models import Chamado, ImageLink,Chat


# Register your models here.

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id','ticket','create','active','username','problem','des_problem','start_datetime','end_datetime','grupo', 'status','finalizado',)
    search_fields = ('id','ticket','create','active','username','problem','des_problem','start_datetime' ,'end_datetime','grupo','status','finalizado',)
    


@admin.register(ImageLink)
class ImageLinkAdmin(admin.ModelAdmin):
    list_display = ('create','active','link', 'img',)
    search_fields =('create','active','link', 'img',)
    
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','idChat','From', 'mensagem','nome',)
    search_fields =('id','create','active','idChat','From','mensagem','nome',)




