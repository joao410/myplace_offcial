from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [   
    path('category',views.category, name="category"),
    path('product/<int:category_code>',views.product, name="product"),
    path('part/<int:product_code>',views.part, name="part"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)