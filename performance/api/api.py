
from os import name
from rest_framework import request, serializers
from rest_framework.serializers import Serializer
from django.db.models import query
from .serializers import Performanceserializer,Announcementserializer
from users.api.serializers import Userserializer
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
from django.contrib.auth.models import Group, User
from django.contrib import auth
from rest_framework.authentication import TokenAuthentication
from performance.models import Performance,Announcement
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from users.models import UsuarioCorporativo, UsuarioPessoal
import pandas as pd
from rest_framework.parsers import FileUploadParser, JSONParser
from decimal import Context, Decimal
from django.utils import timezone
import json
from django.http.response import JsonResponse
from django.db.models import Count

class performance_view(viewsets.ModelViewSet):
    today = timezone.now()
    queryset = Performance.objects.all()
   
    serializer_class = Performanceserializer
    def get(self, request, format=None):

       return 

class announciments_view(viewsets.ModelViewSet):
    serializer_class = Announcementserializer
    queryset = Announcement.objects.all()
