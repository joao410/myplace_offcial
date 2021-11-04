from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.utils import report 
from utils.update import update, update_myplace,list
import os
from ..models import Report_human_resources,Calendar
from datetime import date, datetime, timedelta
from users.models import UsuarioCorporativo
from django.contrib import messages
from os import name
from rest_framework import request, serializers
from rest_framework.serializers import Serializer
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from .serializers import reportserializer,calendarserializer
import pytz

utc=pytz.UTC


class Calendar_view(viewsets.ModelViewSet):
    serializer_class = calendarserializer
    queryset = Calendar.objects.all()
class Reports_views(viewsets.ModelViewSet):
    serializer_class = reportserializer
    queryset = Report_human_resources.objects.all()

class update_view(views.APIView):
    def post(self,format=None):
        update()
        return Response('deu certo')
class mp_update_view(views.APIView):
    def post(self,format=None):
        list()
        return Response('deu certo')        
class Report_view(views.APIView):
    def post(self,format=None):
        today = datetime.now()
        name = 'Relat_Profissionais__' +  today.strftime("%d_%m_%Y_%H_%M") + '.xlsx'
        old_file = os.path.join(settings.MEDIA_ROOT + '\\models_rh\\' + name )
        report_hr = Report_human_resources.objects.filter(file_name = name)
        if len(report_hr) < 2:   
            try:
                os.remove(old_file) 
            except:
                pass    
            report()

            file = Report_human_resources.objects.create(file=old_file, file_name=name)
            file.save()
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        
        return Response(status=status.HTTP_202_ACCEPTED)

class create_calendar_view(views.APIView):
    def post(self, request,format=None):
        start_date = datetime.strptime(request.POST['start_date'] + ":00",'%Y-%m-%d %H:%M:%S')
        start =request.POST['start']
        end =request.POST['end']
        end_date = datetime.strptime(request.POST['end_date'],'%Y-%m-%d %H:%M:%S')
        user = self.request.user
        title = request.POST['title']    
        location=  request.POST['location']   
        start_date =  utc.localize(start_date)
        end_date =  utc.localize(end_date)
        verifications_start= Calendar.objects.filter(start_date_time__gt = start_date, start_date_time__lt=end_date)
        verifications_end= Calendar.objects.filter(end_date_time__gt = start_date ,end_date_time__lt = end_date  )
        if verifications_start or verifications_end:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:   
            Calendar.objects.create(start_date_time=start_date,start=start,data_end=end,end_date_time= end_date,reserve=user,title=title,location=location)
            return Response(status=status.HTTP_201_CREATED)
      
           
    def put(self, request,format=None):
        id =  request.POST["id"]
        reserve = Calendar.objects.get(pk=id)
        reserve.delete()
        return Response(status=status.HTTP_410_GONE)



######## OLD VIEW ###########


# @login_required(login_url='/authentication/login')  
# def report_rh(request):
#     today = datetime.now()
#     name = 'Relat_Profissionais__' +  today.strftime("%d_%m_%Y_%H_%M") + '.xlsx'
#     old_file = os.path.join(settings.MEDIA_ROOT + '\\models_rh\\' + name )
#     report_hr = Report_human_resources.objects.filter(file_name = name)
#     if len(report_hr) < 2:   
#         try:
#             os.remove(old_file) 
#         except:
#             pass    
#         report()

#         file = Report_human_resources.objects.create(file=old_file, file_name=name)
#         file.save()
#     else:
#         messages.error(request,'Limite de relatorios por dia alcançado!! Seu limite são 2 por dia.' )

    
#     return redirect('reports') 

# @login_required(login_url='/authentication/login') 
# def reports(request):
#     usuarioC = UsuarioCorporativo.objects.get(usuario=request.user)
#     grupos= usuarioC.grupo.name
#     report_hr = Report_human_resources.objects.all()
#     try:
#         imageP = ImagePerfil.objects.get(nome= codigo.nome)
#         if not imageP.image:
#             imageP = ImagePerfil.objects.get(nome= "padrao")
#     except:
#         imageP = ImagePerfil.objects.get(nome= "padrao")       
#     if  request.user == 'Administrador':
#         report_hr = Report_human_resources.objects.all()
#         context= {
#         'report_hr':report_hr,
#         } 
#         return render(request,'reports/index.html',context)

#     context= {
#     'report_hr':report_hr,
#     'usuarioC':usuarioC,
#     'grupos':grupos,
#     'imageP':imageP,
#     }    
#     return render(request,'reports/index.html',context)  