from django.contrib import admin
from inventory.models import Category,Product,Product_details,Log_association,Log_defect,Log_entrance



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