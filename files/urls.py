 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from os import name
from files.api.api import Report_view,Reports_views,Calendar_view,create_calendar_view,update_view,mp_update_view
from rest_framework import routers, urlpatterns

router = routers.DefaultRouter()
router.register('all_reports',Reports_views,'all_reports ')
router.register('reservas',Calendar_view,'reservas ')

urlpatterns = [
    
    path('reports/',Report_view.as_view(),name="reports"),
 
    path('criar_reserva/',create_calendar_view.as_view(),name="criar_reserva"),
    path('update/',update_view.as_view(),name="update"),
    path('mpupdate/',mp_update_view.as_view(),name="mpupdate"),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





urlpatterns += router.urls







