from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [   
    # path('category',views.category, name="category"),
    # path('product/<int:category_code>',views.product, name="product"),
    # path('part/<int:product_code>',views.part, name="part"),
    # path('add_category',views.add_category, name="add_category"),
    # path('add_product',views.add_product, name="add_product"),
    # path('add_part',views.add_part, name="add_part"),
    # path('part_dateils/<int:part_code>',views.part_dateils, name="part_dateils"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)