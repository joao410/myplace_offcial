from django.conf import settings
from django.db import models
import uuid
from django.contrib.auth.models import User
import os



class Base(models.Model):
    create = models.DateField('Criacao', auto_now_add=True)
    changed = models.DateField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=False)

    class Meta:
        abstract = True

def get_files_path(_instance, filename):
        ext = filename.split('.')[-1]
        name = filename.split('.')[0]

        filename = f'media/{name}.{ext}'
        return filename

def get_files_path_profile(_instance, filename):
    ext = filename.split('.')[-1]

    filename = f'profile/{uuid.uuid4()}.{ext}'
    return filename

class Announcement(Base):
    name = models.CharField('name', max_length=500)
    sku = models.IntegerField()
    description = models.TextField('description', blank=True)
    description_active = models.BooleanField(default=False)
    description_complete = models.DateTimeField('description_complete', blank=True, null=True)
    images_active = models.BooleanField(default=False)
    editable = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    number_images = models.IntegerField(default=0)
    date_complete = models.DateTimeField('date_complete', blank=True, null=True)
    edit_by = models.CharField('edit_by', max_length=50, blank=True)
    complete = models.BooleanField(default=False)
    user_image = models.CharField('user_image', max_length=30, default='#')
    image_zero = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    image_complete = models.DateTimeField('image_complete', blank=True, null=True)


    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return f'{self.sku} - {self.name}'   
 


class Image(Base):
    name = models.CharField('name', max_length=100, default='#')
    image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    announcement = models.ForeignKey(Announcement ,on_delete=models.CASCADE)
    user = models.CharField('user', max_length=30)
    
   
   

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return f'{self.announcement.sku} - {self.active}'
    def rename_image(self):
        img_full_path = os.path.join(settings.MEDIA_ROOT,self.name)
        img_pill = Image.open(img_full_path)
        img_name = img_pill.name

        os.rename(img_name,f'produto/{self.announcement.sku}/{img_name}')
       
        return rename_image()




class Metas(Base):
    meta = models.IntegerField()

    TYPE_META_CHOICE = {
        ('C.D', 'Criar Descricao'),
        ('E.D', 'Editar Descricao'),
        ('C.F', 'Criar Foto'),
        ('E.F', 'Editar Foto'),
    }  

    type_meta = models.CharField("type_meta", max_length=50, choices=TYPE_META_CHOICE) 
    


    class Meta:
        verbose_name = "Metas"

    def __str__(self):
        return f' {self.meta} - {self.type_meta} '





class Profile(Base):
    metas = models.ManyToManyField(Metas)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to=get_files_path_profile, null=True, blank=True)


    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return f'{self.user}'


class Performance(Base):
    year = models.IntegerField()
    month = models.IntegerField()
    porcentagem = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conclude = models.IntegerField(default=0)
    meta = models.ForeignKey(Metas, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Performance"
        verbose_name_plural = "Performances"

    def __str__(self):
        return f'{self.month} - {self.user}'


class Annou_Detail(Base):
    anuncio = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    detail = models.CharField('annou_detail', max_length=255)

    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"

    def __str__(self):
        return f'{self.anuncio} - {self.detail}'
