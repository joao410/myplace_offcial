
from django.contrib.auth import models
from rest_framework import serializers
from helpdesk.models import  Chamado,Chat,ImageLink




class  Calledserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chamado
        fields= '__all__'