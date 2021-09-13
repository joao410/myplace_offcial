from django.contrib.auth import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Places,Inputs,Manufacturer,Manufacturer_address,Stock_loc,Contacts,Log_association,Log_defect,Log_entrance



######### Inventory Serializers #######

class Manufactureaddressserializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer_address
        fields = '__all__'



class Manufacturerserializer(serializers.ModelSerializer):
    address = Manufactureaddressserializer(many=False)
    class Meta:
        model = Manufacturer
        fields = '__all__'



class Contactserializer(serializers.ModelSerializer):
    manufacturer_code = Manufacturerserializer(many=False)
    class Meta:
        model = Contacts
        fields = '__all__'


class Stockserializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_loc
        fields= '__all__'


class Placeserializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'     

class Inputserializer(serializers.ModelSerializer):
    localization = Placeserializer(many=False)
    manufacturer_code = Manufacturerserializer(many=False) 
    class Meta:
        model = Inputs
        fields = '__all__'
        

class  Logentranceserializer(serializers.ModelSerializer):
    code = Inputserializer(many=False)
    class Meta:
        model = Log_entrance
        fields = '__all__'


class Logassociationserializer(serializers.ModelSerializer):
    code = Inputserializer(many=False)
    class Meta:
        model = Log_association
        fields = '__all__'


class Logdefectsrializer(serializers.ModelSerializer):
    code = Inputserializer(many=False)
    class Meta:
        model= Log_defect
        fields = '__all__'
