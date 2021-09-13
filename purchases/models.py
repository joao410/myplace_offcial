
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import  BooleanField, CharField


from django.db.models.fields.related import ForeignKey
# Create your models here.


class Base(models.Model):
    create = models.DateTimeField('Criacao', auto_now_add=True)
    changed = models.DateTimeField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=False)

    class Meta:
        abstract = True

def get_files_invoice(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'invoice/{uuid.uuid4()}.{ext}'
    return filename

def get_files_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'requisitions/{uuid.uuid4()}.{ext}'
    return filename

class Purchase_requisition(Base):
    purchase_requisition_id = models.IntegerField('id da requisição',primary_key=True)
    sector = models.CharField("setor",max_length=100,blank=True,null=True)
    requester = models.CharField("Requisitante",max_length=100)
    manager = models.CharField("Gestor",max_length=100)
    buyer = models.CharField('Comprador(a)',max_length=100,blank=True,null=True)
    approved = BooleanField("verificação do gestor ",default=False)
    status = models.CharField("status",max_length=255,default="Aguardando verificação do Gestor")
    total_price = models.IntegerField("preço total",blank=True,null=True)
    financial_approval = models.BooleanField("aprovado pelo financeiro",default=False)
    justification = models.CharField("justificativa",max_length=255,blank=True, null=True)
    deadline = models.DateField("Data de entrega esperado",blank=True,null=True)
    forecast = models.CharField("tempo de  consumo",max_length=100 , blank=True,null=True)    
    purchase_manager_approval = models.BooleanField(default=False)
    cotation = models.BooleanField(default=False)
    cot = models.DateTimeField(blank=True,null=True)
    boug = models.DateTimeField(blank=True,null=True)
    note = models.CharField("Observação", max_length=500,blank=True,null=True)
    return_reason= models.CharField("Motivo da devolução", max_length=500,blank=True,null=True)
   

    class Meta:
       verbose_name = "Requisição"
       verbose_name_plural = "Requisições"

    def __str__(self):
        return f'{self.purchase_requisition_id }'

def get_files_ticket(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'tickets/{uuid.uuid4()}.{ext}'
    return filename

def get_files_voucher(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'voucher/{uuid.uuid4()}.{ext}'
    return filename
    
class Requisition_product(Base):
    purchase_requisition_id = models.ForeignKey(Purchase_requisition,on_delete=DO_NOTHING,blank=True,null=True)
    requisition_product = models.CharField("Produto",max_length=255)
    price_product = models.CharField("preço do produto",max_length=20,blank=True,null=True)
    first_provider= models.CharField("primeiro fornecedor",max_length=255,blank=True,null=True)
    second_provider= models.CharField("segundo_fornecedor",max_length=255,blank=True,null=True)
    third_provider= models.CharField("terceiro_fornecedor",max_length=255,blank=True,null=True)
    amount = models.IntegerField('quantidade',default=1)
    unit = models.CharField("unidade",max_length=100,blank=True,null=True)
    first_cotation = models.DecimalField('primeira cotação', max_digits=15,decimal_places=2,blank=True,null=True)
    second_cotation = models.DecimalField('segunda  cotação', max_digits=15,decimal_places=2,blank=True,null=True)
    third_cotation = models.DecimalField('trerceira cotação', max_digits=15,decimal_places=2,blank=True,null=True)
    cotations_length = models.IntegerField("quantidade de cotações",blank=True,null=True,default=0) 
    ticket = models.FileField(upload_to=get_files_ticket ,blank=True,null=True)
    payment_voucher = models.FileField(upload_to=get_files_voucher ,blank=True,null=True)
    type_of_payment = models.CharField("tipo de pagamento" , max_length=100,blank=True,null=True)
    delivered = models.BooleanField(default=False)
    invoice = models.FileField(upload_to=get_files_invoice,blank=True,null=True) 
    delivered_at =models.DateTimeField(blank=True,null=True)
    image= models.ImageField(upload_to=get_files_path,blank=True,null=True)

    class Meta:
       verbose_name = "Produto cotado"
       verbose_name_plural = "Produtos cotados"

    def __str__(self):
        return f'{self.purchase_requisition_id} - {self.requisition_product}'