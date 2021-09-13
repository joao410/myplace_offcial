
from django.db import models
from os import name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, DateTimeField
from utils.utils import report 

from django.db.models.fields.related import ForeignKey
# Create your models here.

class Base(models.Model):
    create = models.DateTimeField('Criacao', auto_now_add=True)
    update = models.DateTimeField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True



def get_banner_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'banners/{uuid.uuid4()}.{ext}'
    return filename
class Report_human_resources(Base):
    file = models.FileField(upload_to='models_rh/',blank=True,null=True) 
    file_name = CharField('nome', max_length=100)
    file_category= CharField('category',max_length=100,blank=True,null=True)
   
    
    class Meta:
       verbose_name = "Relatorio RH"
       verbose_name_plural = "Relatorios RH"

    
    def __str__(self):
        return f'{self.file} - {self.file_name}'    

class Dashbaners(Base):
    image     = models.FileField('banner',upload_to=get_banner_path)
    desc      = models.CharField('Descrição',max_length=255,blank=True,null=True)
    manager   = models.CharField("gestor",max_length=100 ,blank=True,null=True)
    geral     = models.BooleanField(default=False)
    timeshow  = models.CharField("tempo de exibiçao",max_length=4,default='30')
    order_by  = models.IntegerField("ordem de exibição",blank=True,null=True)

    class Meta:
       verbose_name = "dashbaner"
       verbose_name_plural = "dashbaners"

    def __str__(self):
        return f'{self.desc} - {self.manager}'   

  


