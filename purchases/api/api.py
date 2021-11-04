from .serializers import PurchaseRequisitionserializer,ProductRequisitionserializer
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from purchases.models import  Requisition_product,Purchase_requisition
from decimal import Context, Decimal
from django.utils import timezone
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
import json
from django.http.response import JsonResponse
from django.db.models import Count
from users.models import UsuarioCorporativo, UsuarioPessoal
from datetime import datetime
from rest_framework.parsers import FileUploadParser, JSONParser


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