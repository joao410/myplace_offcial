from os import truncate
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, CharField, IntegerField

from django.db.models.fields.related import ForeignKey
from django.db.models.manager import ManagerDescriptor
from django.utils import tree

# Create your models here.


class Base(models.Model):
    create = models.DateField('Criacao', auto_now_add=True)
    update = models.DateField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


def get_files_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'produtos/invoice/{uuid.uuid4()}.{ext}'
    return filename
class Places(Base):
    place = models.CharField("local",max_length=200,blank=True,null=True)
    company = models.CharField('empresa',max_length=100,blank=True,null=True)
    department = models.CharField('departamento',max_length=100,blank=True,null=True)
    class Meta:
       verbose_name = "local de armazenagem"
       verbose_name_plural = "locais de armazenagem"

    def __str__(self):
        return f'{self.place} - {self.company} - {self.department}'   



class Manufacturer_address(Base): 
    address_code = models.IntegerField('codigo do endereço',null=True,blank=True)
    zip_code = models.CharField('cep',max_length=10,null=True,blank=True)
    public_place = models.CharField('Logradouro',max_length=100,blank=True,null=True)
    number = models.IntegerField('Número',null=True,blank=True)
    country = models.CharField('Pais', max_length=100,blank=True,null=True)
    uf = models.CharField('Uf',max_length=2,null=True,blank=True)
    city = models.CharField('Municipio',max_length=100,blank=True,null=True)
    district = models.CharField('Bairro',max_length=100,blank=True,null=True)
    complement = models.CharField('Complemento',max_length=10,null=True,blank=True)

    class Meta:
       verbose_name = "Endereços do fornecedor"
       verbose_name_plural = "Endereços dos fornecedores"

    def __str__(self):
        return f'{self.zip_code} - {self.public_place} - {self.number}'   



class  Manufacturer(Base):
    manufacturer_code= models.IntegerField('codigo',null=True,blank=True)
    person = models.CharField('Pessoa',max_length=100,null=True,blank=True)
    manufacturer = models.CharField('fornecedor',max_length=255,null=True,blank=True)
    fantasy = models.CharField('fantasia',max_length=255,null=True,blank=True)
    industry = models.CharField('Ramo de atividade',max_length=200,null=True,blank=True)
    cpf_cnpj = models.CharField('cpf/cnpj',max_length=30,null=True,blank=True)
    ie_rg = models.CharField('IE/RG',max_length=30,null=True,blank=True)
    ie_indicator = models.CharField('indicador IE',max_length=50,null=True,blank=True)
    type  = models.CharField('tipo',max_length=100,null=True,blank=True)
    telephone1 = models.CharField('Telefone1',max_length=15,null=True,blank=True)
    telephone2 = models.CharField('Telefone',max_length=15,null=True,blank=True)
    e_mail = models.CharField('E-mail',max_length=100,null=True,blank=True)
    tax_email = models.CharField('E-mail fiscal',max_length=100,null=True,blank=True)
    address = models.ForeignKey(Manufacturer_address,on_delete=DO_NOTHING,null=True,blank=True)
    note = models.CharField('obeservasão',max_length=255,blank=True,null=True)


    class Meta:
       verbose_name = "Fornecedor"
       verbose_name_plural = "Fornecedores"

    def __str__(self):
        return f'{self.manufacturer_code} - {self.person} - {self.manufacturer}'   


class Contacts(Base):
    manufacturer_code= models.ForeignKey(Manufacturer,on_delete=CASCADE,null=True,blank=True)
    contact = models.CharField('Contato',max_length=100,null=True,blank=True)
    phone  = models.CharField('tel/Cel',max_length=100,blank=True,null=True)
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f'{self.manufacturer_code} - {self.contact}'   

class Stock_loc(Base):
    road = models.CharField('Rua',max_length=100,null=True,blank=True)
    side = models.CharField('Lado',max_length=100,null=True,blank=True)
    shelf = models.CharField('Pratileira',max_length=100,null=True,blank=True)
    drawer = models.CharField('Graveta',max_length=100,null=True,blank=True)

    class Meta:
       verbose_name = "Localização do estoque "
       verbose_name_plural = "Localizações do estoque"

    def __str__(self):
        return f'{self.road} - {self.drawers}'   



class Inputs(Base):
    description     = models .CharField('descrição',max_length=255,blank=True,null=True)
    code            = models.IntegerField("codigo",blank=True,null=True)
    category        = models.CharField("categoria",max_length=100,blank=True,null=True)
    localization    = models.ForeignKey(Places,on_delete=DO_NOTHING,blank=True,null=True)
    entry_date      = models.DateTimeField(blank=True,null=True)
    type            = models.CharField("tipo",max_length=100,blank=True,null=True)
    amount          = models.IntegerField('quantidade',blank=True,null=True,default=0)
    cost_price      = models.DecimalField('Preço de custo',max_digits=15,decimal_places=2,blank=True,null=True)
    company         = models.CharField('Empresa',max_length=100,blank=True,null=True)
    area            = models.CharField('Area',max_length=100,blank=True,null=True)
    responsible     = models.CharField('Usuário responsavel',max_length=100,blank=True,null=True)
    is_used         = models.BooleanField('em uso',default=False)
    quantity_in_use = models.IntegerField('quantidade em uso',blank=True,null=True,default=0)
    status = models.CharField('status',max_length=100,blank=True,null=True)
    invoice = models.FileField("nota fiscal",upload_to=get_files_path,blank=True,null=True)
    associate = models.CharField('associado',max_length=100,blank=True,null=True)
    surname = models.CharField('apelido',max_length=100,blank=True,null=True)
    manufacturer_code = models.ForeignKey(Manufacturer,on_delete=DO_NOTHING,blank=True,null=True)
    entry_quantitaty = models.IntegerField('quantidade de entrada',blank=True,null=True,default=0)
    output_quantity = models.IntegerField('quantidade de saida',blank=True,null=True,default=0)
    maximum_amount = models.IntegerField('quantidade maxima',blank=True,null=True)
    minimum_quantity = models.IntegerField('quantidade minima',blank=True,null=True)
    note = models.CharField('Observação',max_length=255,blank=True,null=True)
    bar_code = models.CharField('Código de barras',max_length=10,null=True,blank=True)
    available_quantity = models.IntegerField('Quantidade disponivel',blank=True,null=True)
    destination = models.CharField('Destinação',max_length=100,null=True,blank=True)
    shipping_value = models.DecimalField('valor do frete', max_digits=20,decimal_places=2,null=True,blank=True)
    average_cost = models.DecimalField('custo medio',max_digits=20,decimal_places=2,null=True,blank=True )
    end_date = models.DateTimeField('Data que acabou',blank=True,null=True)
    product_type = models.CharField('Tipo de Produto',max_length=100,null=True,blank=True)
    stock_loc = models.ForeignKey(Stock_loc,on_delete=DO_NOTHING,null=True,blank=True)

    class Meta:
       verbose_name = "Insumo"
       verbose_name_plural = "Insumos"

    def __str__(self):
        return f'{self.description} - {self.code}'   




class Log_association(Base):
    association_code = models.IntegerField("codigo da Associação",primary_key=True)
    code = models.ForeignKey(Inputs,on_delete=DO_NOTHING,blank=True,null=True)
    associate = models.CharField('associado',max_length=100,blank=True,null=True)
    creator = models.CharField("criador",max_length=255)
    action = models.CharField("Ação", max_length=100)

    class Meta: 
       verbose_name = "Associação"
       verbose_name_plural = "Associações"

    def __str__(self):
        return f'{self.code} - {self.associate} - {self.association_code}'


class Log_defect(Base):
    defect_code = models.IntegerField("codigo do defeito",primary_key=True)
    code = models.ForeignKey(Inputs,on_delete=DO_NOTHING,blank=True,null=True)
    reason = models.CharField("motivo",max_length=255)
    creator = models.CharField("criador",max_length=255)

    class Meta:
       verbose_name = "Defeito"
       verbose_name_plural = "Defeitos"

    def __str__(self):
        return f'{self.code} - {self.reason}'
    

class Log_entrance(Base):
    entrance_code = models.IntegerField("codigo da entrada", primary_key=True)
    code = models.ForeignKey(Inputs,on_delete=DO_NOTHING,blank=True,null=True)
    creator = models.CharField("criador",max_length=255)

    class Meta:
       verbose_name = "Entrada de peça"
       verbose_name_plural = "Entrada de peças"

    def __str__(self):
        return f'{self.entrance_code}  '




class Log_Movimantation(Base):
    modifyer = models.CharField('atuante',max_length=100,blank=True,null=True)
    description  = models .CharField('descrição',max_length=255,blank=True,null=True)
    code = models.IntegerField("codigo",blank=True,null=True)
    category = models.CharField("categoria",max_length=100,blank=True,null=True)
    localization = models.ForeignKey(Places,on_delete=DO_NOTHING,blank=True,null=True)
    entry_date = models.DateTimeField(blank=True,null=True)
    type = models.CharField("tipo",max_length=100,blank=True,null=True)
    amount = models.IntegerField('quantidade',blank=True,null=True,default=0)
    cost_price = models.DecimalField('Preço de custo',max_digits=15,decimal_places=2,blank=True,null=True)
    company= models.CharField('Empresa',max_length=100,blank=True,null=True)
    area = models.CharField('Area',max_length=100,blank=True,null=True)
    responsible = models.CharField('Usuário responsavel',max_length=100,blank=True,null=True)
    is_used = models.BooleanField('em uso',default=False)
    quantity_in_use = models.IntegerField('quantidade em uso',blank=True,null=True,default=0)
    status = models.CharField('status',max_length=100,blank=True,null=True)
    invoice = models.FileField("nota fiscal",upload_to=get_files_path,blank=True,null=True)
    associate = models.CharField('associado',max_length=100,blank=True,null=True)
    surname = models.CharField('apelido',max_length=100,blank=True,null=True)
    manufacturer_code = models.ForeignKey(Manufacturer,on_delete=DO_NOTHING,blank=True,null=True)
    entry_quantitaty = models.IntegerField('quantidade de entrada',blank=True,null=True,default=0)
    output_quantity = models.IntegerField('quantidade de saida',blank=True,null=True,default=0)
    maximum_amount = models.IntegerField('quantidade maxima',blank=True,null=True)
    minimum_quantity = models.IntegerField('quantidade minima',blank=True,null=True)
    note = models.CharField('Observação',max_length=255,blank=True,null=True)
    bar_code = models.CharField('Código de barras',max_length=10,null=True,blank=True)
    available_quantity = models.IntegerField('Quantidade disponivel',blank=True,null=True)
    destination = models.CharField('Destinação',max_length=100,null=True,blank=True)
    shipping_value = models.DecimalField('valor do frete', max_digits=20,decimal_places=2,null=True,blank=True)
    average_cost = models.DecimalField('custo medio',max_digits=20,decimal_places=2,null=True,blank=True )
    end_date = models.DateTimeField('Data que acabou',blank=True,null=True)
    product_type = models.CharField('Tipo de Produto',max_length=100,null=True,blank=True)
    stock_loc = models.ForeignKey(Stock_loc,on_delete=DO_NOTHING,null=True,blank=True)


    class Meta:
        verbose_name = "Log_movimentação"
        verbose_name_plural = "Log_movimentação"

    def __str__(self):
        return f'{self.description} - {self.code}'   





