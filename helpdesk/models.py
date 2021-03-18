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
    username    =   models.CharField("username", max_length=255, default='#')
    ticket      =   models.CharField("ticket", max_length=5, default="#")
    problem     =   models.TextField(null=True, blank=True, default='#')
    des_problem = models.TextField(null=True, blank=True,default="#")
    obs_tecnico =   models.TextField(null=True, blank=True, default='#')
    name     =   models.ForeignKey(UsuarioPessoal, on_delete=models.DO_NOTHING, null=True, blank=True)
    data = models.CharField("data", max_length=50, default='#')
    finalizado = models.CharField("finalizado" , max_length=100, default="")
    
    grupo = models.CharField("grupo", max_length=20,default="#")

    URGENCY_CHOICES = {
        ('Baixa', 'Baixa'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),

    }
    urgency = models.CharField("urgencia", max_length=10, choices=URGENCY_CHOICES, default="#")
    
    STATUS_CHOICES = {
        ('aberto', 'aberto'),
        ('aguardando', 'aguardando'),
        ('em atendimento', 'em atendimento'),
        ('fechado', 'fechado'),

    }
    status  =   models.CharField("status", max_length=100,choices=STATUS_CHOICES,  default='aberto')


    class Meta:
       verbose_name = "Chamado"
       verbose_name_plural = "Chamados"

    def __str__(self):
        return f'{self.id} - {self.urgency}' 


def get_files_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'chamado/images/{uuid.uuid4()}.{ext}'
    return filename





class Image(Base):
    nome = models.CharField("nome", max_length=100,default="#")
    image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, default=None)
    ticket =  models.CharField('ticket', max_length=50, default="#")
    obs = models.TextField(null=True, blank=True, default='#')
   
   
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
    From= models.CharField("from", max_length=100,default="")
    idChat = models.ForeignKey(Chamado, on_delete=models.CASCADE,null=True,blank=True)
    mensagem = models.CharField("mensagem", max_length=205, default="#")
    nome = models.CharField("nome",max_length=100,default="")
    

    class Meta:
       verbose_name = "Chat"
       verbose_name_plural = "Chats"


    def __str__(self):
        return f'{self.id} - {self.mensagem}' 














