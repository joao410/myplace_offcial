from  .serializers import Calledserializer
from helpdesk.models import Chamado
from rest_framework.parsers import FileUploadParser, JSONParser
from decimal import Context, Decimal
from django.utils import timezone
import json
from django.http.response import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
from django.contrib.auth.models import Group, User
from django.contrib import auth
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from users.models import UsuarioCorporativo, UsuarioPessoal
from users.api.serializers import Userserializer



class called_by_group_view(viewsets.ModelViewSet):
    permission_classes= (IsAuthenticated,)
    serializer_class = Calledserializer
    def get_queryset(self):
        users = UsuarioCorporativo.objects.get(user=self.request.user)
        query = Chamado.objects.filter(grupo= users.group).order_by("status")
        return query

class called_by_name_view(viewsets.ModelViewSet):
    permission_classes= (IsAuthenticated,)
    serializer_class = Calledserializer

    def get_queryset(self):
        query = Chamado.objects.filter(username = self.request.user.username).order_by("status")
        return query

class called_view(viewsets.ModelViewSet):
    serializer_class = Calledserializer

    def get_queryset(self, format=None):
        
        query = Chamado.objects.all()
        return query
       
class maneger_View(viewsets.ModelViewSet):
    permission_classes= (IsAuthenticated,)
    serializer_class = Userserializer
    def get_queryset(self,format=None):
        list_manager = ['gestor']
        query = User.objects.filter(groups__name__in=list_manager)
        return query

class called_grafics_views(views.APIView):
    serializer_class = Calledserializer
    def get(self,format=None):
        ti_problem_chart = Chamado.objects.filter(grupo='atendimento ti').values('grupo','problem').annotate(total=Count('problem')).order_by('problem')
        ti_company_chart = Chamado.objects.filter(grupo='atendimento ti').values('grupo','company').annotate(total=Count('company')).order_by('company')
        ti_finished_chart = Chamado.objects.filter(grupo='atendimento ti').values('grupo','finalizado').annotate(total=Count('finalizado')).order_by('finalizado')
        rh_problem_chart = Chamado.objects.filter(grupo='recursos humanos').values('grupo','problem').annotate(total=Count('problem')).order_by('problem')
        rh_company_chart = Chamado.objects.filter(grupo='recursos humanos').values('grupo','company').annotate(total=Count('company')).order_by('company')
        rh_finished_chart = Chamado.objects.filter(grupo='recursos humanos').values('grupo','finalizado').annotate(total=Count('finalizado')).order_by('finalizado')
        new_object =[ti_problem_chart,ti_company_chart,ti_finished_chart,rh_problem_chart,rh_company_chart,rh_finished_chart]
        return Response(new_object)

class create_call_View(views.APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Calledserializer
    parser_class = (FileUploadParser,)
    def post(self,request,format=None):
        if Chamado.objects.all():
            chamado_id = Chamado.objects.all().order_by('-id')[0].id
                

            ticket = chamado_id + 10001
        else:
                        ticket = 10001
        subject = request.POST["subject"]
        message = request.POST["message"]
        try:
            attachment =request.FILES["attachment"]
        except:
            attachment ="C:\\Users\\arena\\projeto_python\\myplace\\media\\chamado\\images\\padrao.png"
        grupo = request.POST["grupo"]
        status_chamado="aberto"
        fin = ""
        urgency="baixa"
        name = ''
        data = timezone.now()
        user = self.request.user
        Chamado.objects.create(username=user,name=name,problem=subject,status=status_chamado,data=data,ticket=ticket,finalizado=fin,urgency=urgency,grupo=grupo,des_problem=message,file=attachment)
      
        return Response(status=status.HTTP_202_ACCEPTED)

class called_by_idView(views.APIView):
    permission_classes= (IsAuthenticated,)

    def get_object(self,id):
        try:
           return Chamado.objects.get(pk=id)
        except:
            raise Http404    
    def get(self,request,id,format=None):
        id = self.get_object(id)
        Serializer = Calledserializer(id)
        return  Response(Serializer.data)
       
class answer_call_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Chamado.objects.get(pk=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        chamado = Chamado.objects.get(pk=id)
        chamado.status = "em atendimento"
        chamado.name = user.code.name
        chamado.save()
        return Response(status=status.HTTP_202_ACCEPTED)

class end_call_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Chamado.objects.get(pk=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        chamado = Chamado.objects.get(pk=id)
        chamado.status = "resolvido"
        chamado.finalizado = user.code.name
        chamado.end_datetime = timezone.now()
        chamado.active= False
        chamado.save()
        return Response(status=status.HTTP_202_ACCEPTED)
        
class reopen_call_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Chamado.objects.get(pk=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
      
        chamado = Chamado.objects.get(pk=id)
        chamado.status = "aberto"
        chamado.active = True
        chamado.save()
        return Response(status=status.HTTP_202_ACCEPTED)

class redirect_call_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Chamado.objects.get(pk=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
      
        chamado = Chamado.objects.get(pk=id)
        if chamado.grupo == "atendimento ti":
            chamado.grupo = "recursos humanos"
            chamado.save()
        else :
            chamado.grupo = "atendimento ti"
            chamado.save()   
        return Response(status=status.HTTP_202_ACCEPTED)
        