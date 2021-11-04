
from rest_framework import serializers
from django.contrib.auth import models
from rest_framework import request, serializers
from rest_framework.parsers import FileUploadParser, JSONParser
from decimal import Context, Decimal
from django.utils import timezone
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
import json
from django.http.response import JsonResponse
from django.db.models import Count
from purchases.models import  Requisition_product,Purchase_requisition


class PurchaseRequisitionserializer(serializers.ModelSerializer):
    class Meta :
        model = Purchase_requisition
        fields = '__all__'

class ProductRequisitionserializer(serializers.ModelSerializer):
    class Meta :
        model = Requisition_product
        fields = '__all__'