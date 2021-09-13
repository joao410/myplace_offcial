from django.contrib import admin
from .models import Announcement, Image,  Metas, Profile, Performance


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'user', 'editable', 'active', 'create')
    search_fields =  ('sku', 'name', 'user', 'editable', 'active', 'create')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('announcement', 'user', 'image', 'create')
    search_fields = ('announcement', 'user', 'image', 'create')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', 'metas',)


@admin.register(Metas)
class MetasAdmin(admin.ModelAdmin):
    list_display = ('meta', 'type_meta',)
    search_fields = ('meta', 'type_meta',)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('month', 'year', 'user', 'conclude', 'porcentagem')
    search_fields = ('month', 'year', 'user', 'conclude', 'porcentagem')