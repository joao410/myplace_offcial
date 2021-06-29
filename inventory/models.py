from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, CharField

from django.db.models.fields.related import ForeignKey

# Create your models here.


class Base(models.Model):
    create = models.DateField('Criacao', auto_now_add=True)
    update = models.DateField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField("nome", max_length=100)
    amount = models.IntegerField("quantidade", blank=True,default=0)
    category_code = models.IntegerField("cod_categoria",primary_key=True)


    class Meta:
        abstract = True

    class Meta:
       verbose_name = "categoria"
       verbose_name_plural = "categorias"

    def __str__(self):
        return f'{self.name} - {self.amount}'


class Product(Base):
    brand = models.CharField("marca",max_length=254)
    model = models.CharField("modelo",max_length=100)
    amount = models.IntegerField("quantidade_produto",blank=True,default=0)
    product_code = models.IntegerField("codigo produto",primary_key=True,)
    category_code = ForeignKey(Category,on_delete=CASCADE)

    class Meta:
        abstract = True

    class Meta:
       verbose_name = "Produto"
       verbose_name_plural = "Produtos"

    def __str__(self):
        return f'{self.product_code} - {self.amount}'

class Product_details(Base):
    part_code = models.IntegerField("codigo da peça",primary_key=True,)
    product_code = ForeignKey(Product,on_delete=CASCADE)      
    associate = ForeignKey(User,on_delete=DO_NOTHING,blank=True,null=True)
    details = models.CharField("detalhes da peça",max_length=255)
    defect = BooleanField(default=False)
    used = BooleanField(default=False)

    class Meta:
        abstract = True

    class Meta:
       verbose_name = "Peça"
       verbose_name_plural = "Peças"

    def __str__(self):
        return f'{self.part_code} - {self.associate}'

class Log_association(Base):
    association_code = models.IntegerField("codigo da Associação",primary_key=True)
    part_code = ForeignKey(Product_details,on_delete=DO_NOTHING)
    associate = ForeignKey(User,on_delete=DO_NOTHING)
    creator = models.CharField("criador",max_length=255)
    action = models.CharField("Ação", max_length=100)

    class Meta:
        abstract = True

    class Meta:
       verbose_name = "Associação"
       verbose_name_plural = "Associações"

    def __str__(self):
        return f'{self.part_code} - {self.associate} - {self.association_code}'


class Log_defect(Base):
    defect_code = models.IntegerField("codigo do defeito",primary_key=True)
    part_code = ForeignKey(Product_details,on_delete=DO_NOTHING)
    reason = models.CharField("motivo",max_length=255)
    creator = ForeignKey(User,on_delete=DO_NOTHING)

    class Meta:
        abstract = True

    class Meta:
       verbose_name = "Defeito"
       verbose_name_plural = "Defeitos"

    def __str__(self):
        return f'{self.part_code} - {self.reason}'
    

class Log_entrance(Base):
    entrance_code = models.IntegerField("codigo da entrada", primary_key=True)
    part_code = ForeignKey(Product_details,on_delete=DO_NOTHING)
    product_code = ForeignKey(Product,on_delete=DO_NOTHING)
    creator = ForeignKey(User,on_delete=DO_NOTHING)
    amount = models.IntegerField("quantidade",default=0) 

    class Meta:
        abstract = True

    class Meta:
       verbose_name = "Entrada"
       verbose_name_plural = "Entradas"

    def __str__(self):
        return f'{self.entrance_code} - {self.part_code} - {self.amount}'



    

