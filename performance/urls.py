from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('anuncio/<int:sku>', views.announcement, name='anuncio'),
    path('anuncios_completos', views.complete_anno, name='anuncios-completos'),
    path('pesquisar', views.search_page, name='pesquisar'),
    path('tarefas', views.tasksView, name='tasks'),
    path('del-image-zero/<int:sku>', views.del_image_zero, name='del_image_zero'),
    path('del-images-anno/<int:id>', views.del_image_anno, name='del_image_anno'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
