 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
 path('',views.reports, name="reports"),
 path('report_rh',views.report_rh, name="report_rh"),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)