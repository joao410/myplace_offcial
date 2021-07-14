from django.contrib import admin
from inventory.models import Category,Product,Product_details,Log_association,Log_defect,Log_entrance,Log_cat_entrance,Log_pro_entrance



# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','category_code','name','amount',)
    search_fields =('create','active','update','category_code','name','amount',)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','category_code','product_code','brand','model','amount',)
    search_fields =('create','active','update','category_code','product_code','brand','model','amount',)
@admin.register(Product_details)
class Product_detailsAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','part_code','product_code','associate','details','defect','used')
    search_fields = ('create','active','update','part_code','product_code','associate','details','defect','used')
@admin.register(Log_entrance)
class Log_entranceAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','part_code','product_code','entrance_code','creator')
    search_fields = ('create','active','update','part_code','product_code','entrance_code','creator')
@admin.register(Log_cat_entrance)
class Log_cat_entranceAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','cat_entrance_code','category_code','creator')
    search_fields = ('create','active','update','cat_entrance_code','category_code','creator')
@admin.register(Log_pro_entrance)
class Log_pro_entranceAdmin(admin.ModelAdmin):
    list_display = ('create','active','update','pro_entrance_code','product_code','category_code','creator')
    search_fields = ('create','active','update','pro_entrance_code','product_code','category_code','creator')