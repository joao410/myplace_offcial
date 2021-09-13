
from os import name
from rest_framework import request, serializers

from rest_framework.serializers import Serializer
from helpdesk.models import Chamado
from django.db.models import query
from  .serializers import Calledserializer, Performanceserializer,PurchaseRequisitionserializer,ProductRequisitionserializer,Userserializer
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
from django.contrib.auth.models import Group, User
from django.contrib import auth
from rest_framework.authentication import TokenAuthentication
from performance.models import Performance
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from users.models import UsuarioCorporativo, UsuarioPessoal
from purchases.models import Purchase_requisition,Requisition_product
import pandas as pd
from rest_framework.parsers import FileUploadParser, JSONParser
from decimal import Context, Decimal
from django.utils import timezone
import json
from django.http.response import JsonResponse


from django.http import JsonResponse
# Create your views here.
##### Api view #####



class users_view(viewsets.ModelViewSet):
    
    serializer_class=Userserializer
    queryset = User.objects.all()

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

class purchases_View(viewsets.ModelViewSet):
    serializer_class = PurchaseRequisitionserializer
    def get_queryset(self,format=None):
        query = Purchase_requisition.objects.all()
        return query
        
class purchases_by_name_View(viewsets.ModelViewSet):
    serializer_class = PurchaseRequisitionserializer
    def get_queryset(self,format=None):
        query = Purchase_requisition.objects.filter(requester=self.request.user)
        return query


class performance_view(viewsets.ModelViewSet):
    today = timezone.now()
    queryset = Performance.objects.all()
   
    serializer_class = Performanceserializer
    def get(self, request, format=None):

       return 

########## API VIEW ######


   ###### called ####



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
        

####### purchases #######

class create_req_View(views.APIView):
    permission_classes=(IsAuthenticated,)
    def post(self,request,format=None):
        if Purchase_requisition.objects.all():
            purchases_id = Purchase_requisition.objects.all().order_by('-purchase_requisition_id')[0].purchase_requisition_id
            
            codigo = purchases_id + 6000
        else:
                codigo = 6001
        user = self.request.user
        length= int(request.POST["length"])
        manager = request.POST["manager"]
        sector = request.POST["sector"]
        justify= request.POST["justify"]
        produtos =json.loads(request.POST["produtos"])
        status_req= "aguardando aprovação do gestor"
        deadline = datetime.strptime(request.POST["deadline"],'%d/%m/%Y') 
        forecast = request.POST["forecast"]

        req = Purchase_requisition.objects.create(purchase_requisition_id=codigo,sector=sector,requester=user,manager=manager,status=status_req,justification=justify,deadline=deadline,forecast=forecast)
        
        for product in produtos:
            amount = product["amount"]
            unit =product["unit"]
            product =  product["product"]
            req_prod =Requisition_product.objects.create(purchase_requisition_id = req,amount=amount,unit=unit,requisition_product=product)
            req_prod.save()
        return Response(status=status.HTTP_202_ACCEPTED)    

class req_by_id_View(views.APIView):
    permission_classes= (IsAuthenticated,)

    def get_object(self,id):
        try:
           return Purchase_requisition.objects.get(pk=id)
        except:
            raise Http404    
    def get(self,request,id,format=None):
        id = self.get_object(id)
        Serializer =PurchaseRequisitionserializer(id)
        return  Response(Serializer.data)

class req_prod_by_id_View(views.APIView):
    permission_classes= (IsAuthenticated,)

    def get_object(self,id):
        try:
           return Requisition_product.objects.filter(purchase_requisition_id=id)
        except:
            raise Http404    
    def get(self,request,id,format=None):
        id = self.get_object(id)
        Serializer =ProductRequisitionserializer(id)
        return  Response(Serializer.data)

class  req_val_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        req = Purchase_requisition.objects.get(purchase_requisition_id=id)
        req.status = "aguardando cotação"
        req.approved = True
        req.save()

        return Response(status=status.HTTP_202_ACCEPTED)

class  req_den_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,id):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=id)
        except:
            raise Http404   
   

    def put(self,request,id,format=None):
        req = Purchase_requisition.objects.get(purchase_requisition_id=id)
        req.status = "negado"
        req.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class  req_cot_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Requisition_product.objects.get(pk=request.POST["id"])
        except:
            raise Http404   
   

    def post(self,request,format=None):
        
        req_prod = Requisition_product.objects.get(pk=request.POST["id"])
        if not req_prod.first_cotation:
            req_prod.first_cotation = request.POST["cotation"]
            req_prod.first_provider = request.POST["provider"]
            req_prod.cotations_length =1
            req_prod.save()
        elif not req_prod.second_cotation:
            req_prod.second_cotation = request.POST["cotation"]
            req_prod.second_provider =request.POST["provider"]
            req_prod.cotations_length =2
            req_prod.save()
        else:    
            req_prod.third_cotation = request.POST["cotation"]
            req_prod.third_provider = request.POST["provider"]
            req_prod.cotations_length =3
            req_prod.save()        

        return Response(status=status.HTTP_202_ACCEPTED)
    def put(self,request,format=None):
        req= Purchase_requisition.objects.get(purchase_requisition_id=request.POST["pk"])
        req.cotation = True
        req.buyer = str(self.request.user)
        req.cot = datetime.now()
        req.status ="aguardando aprovação do(a) gestor(a) de compras"
        req.note = request.POST["note"]
        req.save()
        return Response(status=status.HTTP_202_ACCEPTED)

class req_View(views.APIView):
    

    def get(self,request,format=None):
        reqs =Purchase_requisition.objects.all()
        list = []
        for req in reqs:
            prods = Requisition_product.objects.filter(purchase_requisition_id=req.purchase_requisition_id)
            list.append([req,prods])
            

        return  JsonResponse(list)

class req_bou_man_appr_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        except:
            raise Http404    
    def put(self,request,format=None):
        req =  Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        req.purchase_manager_approval =True
        total = 0
        products = Requisition_product.objects.filter(purchase_requisition_id=request.POST["id"])
        prece_products =json.loads(request.POST["prece_product"])
        for i in range(len(products)):
            price_product = prece_products[i]
            products.i.price_product = price_product
            products.i.save()
            total = total + (Decimal(price_product.replace(',','.'))*products.i.amount)
        if total > 1000:
           req.status="aguardando aprovação financeira"  
           req.total_price = total 
           req.save()

        else:
            req.financial_approval = True
            req.status="aprovado"   
            req.total_price = total 
            req.save()    
        return Response(status=status.HTTP_202_ACCEPTED)  

class fin_appr_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        except:
            raise Http404    
    def put(self,request,format=None):
        req =  Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        req.status = "aprovado"
        req.financial_approval = True
        req.save()
        return Response(status=status.HTTP_202_ACCEPTED)     
    
class boug_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        except:
            raise Http404    

    def put(self,request,format=None):
        req =  Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])  
        prods =Requisition_product.objects.filter(purchase_requisition_id=request.POST["id"])
        type_products = json.loads(request.POST["type_products"])
        tickets =  json.loads(request.FILES["tickets"])
        for i in range(len(prods)):
                
                prods.i.type_of_payment = type_products[i]
                try: 
                    form = tickets[i]
                except:
                    form = None
                prods.i.ticket = form
                prods.i.save()     
        req.status="aguardando pagamento"
        req.boug= timezone.now()
        req.save()    
        return Response(status=status.HTTP_202_ACCEPTED)     

class pay_req_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        except:
            raise Http404    
    def put(self,request,format=None):
        req =  Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])  
        prods =Requisition_product.objects.filter(purchase_requisition_id=request.POST["id"])
        vouchers = json.loads(request.POST["vouchers"])
        for i in range(len(prods)): 
                try: 
                    form = vouchers[i]
                except:
                    form = None
                prods.i.payment_voucher = form
                prods.i.save()
        req.status = "comprado"
        req.save() 
        return Response(status=status.HTTP_202_ACCEPTED) 

class del_req_by_prod_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    def get_object(self,request):
        try:
            return Requisition_product.objects.get(pk = request.POST["pk"])
        except:
            raise Http404    
    def post(self,request,format=None):
        prod = Requisition_product.objects.get(pk = request.POST["pk"])
        try: 
            form =  request.FILES["invoice"+str(prod.id)]
        except:
            form = None   
        prod.invoice = form
        prod.delivered = True
        prod.delivered_at = timezone.now()
        prod.save()
        return Response(status=status.HTTP_202_ACCEPTED) 

    def put(self,request,format=None):
        req = Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
        req.status = "entregue"
        req.save()
        return Response(status=status.HTTP_202_ACCEPTED) 

class ret_req_View(views.APIView):
        permission_classes= (IsAuthenticated,)
        def get_object(self,request):
            try:
                return Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])
            except:
                raise Http404    
        def put(self,request,format=None):
            req =  Purchase_requisition.objects.get(purchase_requisition_id=request.POST["id"])  
            req.return_reason = request.POST["reason"]
            req.status = "devolvido"
            req.save()
            return Response(status=status.HTTP_202_ACCEPTED)      




class purchase_View(views.APIView):
    permission_classes= (IsAuthenticated,)
    parser_classes = [JSONParser]
    def get(self,request,format=None):
        reqs =Purchase_requisition.objects.all()
        list = []
        for req in reqs:
            prods = Requisition_product.objects.filter(purchase_requisition_id=req.purchase_requisition_id)
            list.append([req,prods])
  
        return  Response(list)
       