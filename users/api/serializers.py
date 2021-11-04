from django.contrib.auth import models
from django.db.models import fields
from rest_framework import permissions, serializers
from ..models import Contabancaria, UsuarioCorporativo,UsuarioDocumentos,UsuarioPessoal,UsuarioEndereco,UsuarioTrabalho,Office,Companies,Department,Area,Notes
from files.models import  Dashbaners
from django.contrib.auth.models import User,Group
from django.contrib.auth.models import User,Permission

 ###### DJANGO USER #####
class Permissionserializer(serializers.ModelSerializer):
      class Meta:
        model= Permission
        fields = '__all__'
class Userserializer(serializers.ModelSerializer):
    user_permissions= Permissionserializer(many=True)
    class Meta:
        model= User
        fields = ("username",
                "groups",
                "user_permissions",
                )


class Groupserializer(serializers.ModelSerializer):
     permissions = Permissionserializer(many=True)
     class Meta:
        model= Group
        fields = '__all__'


class Dashbanerserializer(serializers.ModelSerializer):
    class Meta:
        model= Dashbaners
        fields = '__all__'

class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model= Companies
        fields = '__all__'

class Areaserializer(serializers.ModelSerializer):
    company = Companyserializer(many=False)
    class Meta:
        model= Area
        fields = '__all__'

class Departmentserializer(serializers.ModelSerializer):
    area = Areaserializer(many=False)
    class Meta:
        model= Department
        fields = '__all__'

class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model= Notes
        exclude = ("update",)

class Officeserializer(serializers.ModelSerializer):
    department = Departmentserializer(many=False)
    class Meta:
        model= Office
        fields = '__all__'

class PernonalUserserializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioPessoal
        fields = '__all__'
        
class WorkUserserializer(serializers.ModelSerializer):

    company =  Companyserializer(many=False)
    department = Departmentserializer(many=False)
    office = Officeserializer(many=False)
    class Meta:
        model= UsuarioTrabalho
        fields = '__all__'

class DocumentUserserializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioDocumentos
        fields = '__all__'

class AddressUserserializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioEndereco
        fields = '__all__'

class Bankserializer(serializers.ModelSerializer):
    class Meta:
        model= Contabancaria
        fields = '__all__'
   
class CorporateUserserializer(serializers.ModelSerializer):
    group = Groupserializer(many=False)
    code = PernonalUserserializer(many=False)
    work = WorkUserserializer(many= False)
    address = AddressUserserializer(many=False)
    document = DocumentUserserializer(many=False)
    bank = Bankserializer(many=False)
    user = Userserializer(many=False)
    
    class Meta:
        model=  UsuarioCorporativo
        fields = '__all__'

    