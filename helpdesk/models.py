from django.db import models
from users.models import UsuarioCorporativo,UsuarioDocumentos,UsuarioEndereco,UsuarioPessoal,UsuarioTrabalho,Empresa,Cargo,ImagePerfil
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
#from users.models import username
#from tecnico.models import name

# Create your models here.



class Base(models.Model):
    create = models.DateField('Criacao', auto_now_add=True)
    update = models.DateField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Chamado(Base):

    #id_chamado = models.CharField("id", max_length=255)s
    username    =   models.CharField("username", max_length=255,default=None)
    ticket      =   models.CharField("ticket", max_length=5,default=None)
    problem     =   models.TextField(null=True, blank=True, default=None)
    des_problem = models.TextField(null=True, blank=True,default=None)
    obs_tecnico =   models.TextField(null=True, blank=True, default=None)
    name     =   models.ForeignKey(UsuarioPessoal, on_delete=models.DO_NOTHING, null=True, blank=True)
    data = models.CharField("data", max_length=50,default=None)
    finalizado = models.CharField("finalizado" , max_length=100, default=None)
    
    grupo = models.CharField("grupo", max_length=20,default=None)

    URGENCY_CHOICES = {
        ('Baixa', 'Baixa'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),

    }
    urgency = models.CharField("urgencia", max_length=10, choices=URGENCY_CHOICES,default=None)
    
    STATUS_CHOICES = {
        ('aberto', 'aberto'),
        ('aguardando', 'aguardando'),
        ('em atendimento', 'em atendimento'),
        ('resolvido', 'resolvido'),

    }
    status  =   models.CharField("status", max_length=100,choices=STATUS_CHOICES,  default='aberto')


    class Meta:
       verbose_name = "Chamado"
       verbose_name_plural = "Chamados"
       ordering = ['-ticket']

    def __str__(self):
        return f'{self.id} - {self.urgency}' 


def get_files_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'chamado/images/{uuid.uuid4()}.{ext}'
    return filename





class Image(Base):
    nome = models.CharField("nome", max_length=100,default=None)
    image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    ticket =  models.CharField('ticket', max_length=50, default=None)
    obs = models.TextField(null=True, blank=True, default=None)
   
   
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Imagens"


    def __str__(self):
        return f'{self.id} - {self.nome}'    
        

class ImageLink(Base):
    img = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    link = models.CharField("link", max_length=255,)
    
    


   
   
    class Meta:
       verbose_name = "ImageLink"
       verbose_name_plural = "ImageLinks"

    def __str__(self):
        return f'{self.id} - {self.link}'    


class Chat(Base):
    From= models.CharField("from", max_length=100,default=None)
    idChat = models.ForeignKey(Chamado, on_delete=models.CASCADE,null=True,blank=True)
    mensagem = models.CharField("mensagem", max_length=205,default=None)
    nome = models.CharField("nome",max_length=100,default=None)
    

    class Meta:
       verbose_name = "Chat"
       verbose_name_plural = "Chats"


    def __str__(self):
        return f'{self.id} - {self.mensagem}' 














