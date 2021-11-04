
from django.contrib.auth import models
from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from helpdesk.models import  Chamado,Chat,ImageLink
from users.models import UsuarioCorporativo,UsuarioDocumentos,UsuarioPessoal,UsuarioEndereco,UsuarioTrabalho,Office,Companies,Department,Area
from performance.models  import Announcement,Performance,Profile,Annou_Detail,Metas
from ..models import  Report_human_resources,Calendar

from django.contrib.auth.models import User,Permission


class calendarserializer(serializers.ModelSerializer):
      class Meta:
          model= Calendar
          fields = '__all__'

 ###### DJANGO USER #####
class reportserializer(serializers.ModelSerializer):
      class Meta:
        model= Report_human_resources
        fields = '__all__'