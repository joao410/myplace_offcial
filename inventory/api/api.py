from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import views
from ..models import Log_defect,Log_entrance,Log_association,Places,Contacts,Manufacturer,Manufacturer_address,Inputs,Stock_loc,Log_Movimantation
from .serializers import Logassociationserializer,Logdefectserializer,Logentranceserializer,Stockserializer,Inputserializer,Manufactureaddressserializer,Manufacturerserializer,Placeserializer,Contactserializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView, Response
from users.models import UsuarioCorporativo
from django.http import Http404
from datetime import date, datetime, timedelta

# Create your views here.

                                                                    ###### API ########

# ##########    Modelsviewset   ########


class product_patrimony_view(viewsets.ModelViewSet):
    serializer_class =  Inputserializer
    # permission_classes =  (IsAuthenticated,)
    def get_queryset(self,format=None):
        # users = UsuarioCorporativo.objects.get(user=self.request.user)
        query = Inputs.objects.filter(destination = "patrimonio")
        return  query

class product_input_view(viewsets.ModelViewSet):
    serializer_class =  Inputserializer
    # permission_classes =  (IsAuthenticated,)
    def get_queryset(self,format=None):
        # users = UsuarioCorporativo.objects.get(user=self.request.user)
        query = Inputs.objects.filter(destination = "insumo")
        return  query

class product_sales_view(viewsets.ModelViewSet):
    serializer_class =  Inputserializer
    # permission_classes =  (IsAuthenticated,)
    def get_queryset(self,format=None):
        # users = UsuarioCorporativo.objects.get(user=self.request.user)
        query = Inputs.objects.filter(destination = "produto")
        return  query

class   Product_by_company_View(viewsets.ModelViewSet):
    serializer_class =  Inputserializer
    permission_classes =  (IsAuthenticated,)
    def get_object(self,company):
        try:
           return Inputs.objects.filter(company=company)
        except:
            raise Http404  
    def get_queryset(self,company):
        category = self.get_object(company)
        Serializer =Inputserializer(company)
        return  Response(Serializer.data)

class   Product_by_category_View(viewsets.ModelViewSet):
    serializer_class =  Inputserializer
    permission_classes =  (IsAuthenticated,)
    def get_object(self,category,company):
        try:
           return Inputs.objects.filter(category=category,company=company)
        except:
            raise Http404  
    def get_queryset(self,category,company):
        category = self.get_object(category,company)
        Serializer =Inputserializer(category,company)
        return  Response(Serializer.data)




#############        API View   ##############

class register_product_view(views.APIView):
    def get_object(self,code):
        try:
            return Inputs.objects.get(code=code)
        except:
            raise Http404    
    def get(self,request,code,format=None):
        code = self.get_object(code)
        Serializer = Inputserializer(code)
        return  Response(Serializer.data)
    def post(self,request,format=None):
        if Log_entrance.objects.all():
                    log_id = Log_entrance.objects.all().order_by('-entrance_code')[0].entrance_code
                    codigo =  log_id  + 1
        else:
                            codigo = 101
        code = request.POST["code"]
        
        if Inputs.objects.filter(code=code).exists():
            return Response(status=status.HTTP_208_ALREADY_REPORTED )
        else:
            description = request.POST["description"]
            category = request.POST["category"]
            localization = request.POST["localization"]
            entry = datetime.today()
            manufacturer_id = request.POST["manufacturer"]
            type = request.POST["type"]
            cost_price  = request.POST["cost_price"]
            company = request.POST['company']
            area  = request.POST["area"]
            status_product = request.POST["status"]
            destination = request.POST["destination"]
            code_bar = request.POST['code_bar']
            amount_entry = request.POST['amount_entry']
            max_amount = request.POST['max_amount']
            minimum_quantity = request.POST['minimum_quantity']
            try:
                local =  Places.objects.get(place=localization)
            except:
                local =  None
            try:    
                manufacturer = Manufacturer.objects.get(manufacturer=manufacturer_id)
            except:
                manufacturer = None   


            new_product=Inputs.objects.create(description=description,code=code,category=category,type=type,cost_price=cost_price,localization=local,destination=destination,area=area,status=status_product,company=company,entry_date=entry,entry_quantitaty=amount_entry,manufacturer_code=manufacturer,bar_code=code_bar,amount=amount_entry,maximum_amount=max_amount,minimum_quantity=minimum_quantity)       


                    ######## LOG ########
            Log_entrance.objects.create(entrance_code=codigo,code=new_product,creator=self.request.user)
            return Response(status=status.HTTP_201_CREATED )  
    def put(self,request,format=None):
        code = request.POST["code"]
        if Inputs.objects.filter(code=code).exists():
            code_bar = request.POST['code_bar']
            type = request.POST["type"]
            cost_price  = request.POST["cost_price"]
            company = request.POST['company']
            area  = request.POST["area"]
            status_product = request.POST["status"]
            destination = request.POST["destination"]
            max_amount = request.POST['max_amount']
            minimum_quantity = request.POST['minimum_quantity']
            description = request.POST["description"]
            
            category = request.POST["category"]
            localization = request.POST["localization"]
            manufacturer_id = request.POST["manufacturer"]
            try:    
                product_output = request.POST['product_output']
            except:
                product_output = 0
            try:    
                product_entry = request.POST['product_entry']
            except:
                product_entry = 0    
            try:
                local =  Places.objects.get(place=localization)
            except:
                local =  None
            try:    
                manufacturer = Manufacturer.objects.get(manufacturer=manufacturer_id)
            except:
                manufacturer = None  
            product = Inputs.objects.get(code=code)
            product.maximum_amount =  max_amount
            product.minimum_quantity = minimum_quantity 
            product.description = description
            product.code = code
            product.category = category
            product.localization = local
            product.manufacture = manufacturer
            product.bar_code = code_bar
            product.destination=destination
            product.status=status_product
            product.company=company
            product.area=area 
            product.cost_price=cost_price 
            product.type=type

            if product_output and not product_entry:
                final_amount = product.amount -  int(product_output)
                if int(product.minimum_quantity) <= final_amount :
                    product.amount =  product.amount - int(product_output) 
                    product.output_quantity = product.output_quantity + int(product_output) 
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)       

                Log_Movimantation.objects.create(modifyer=self.request.user,description=description,code=code,type=type,cost_price=cost_price,destination=destination,status=status_product,company=company,area=area,category=category,localization=local,output_quantity=product_output,manufacturer_code=manufacturer,bar_code=code_bar,amount=product.amount,maximum_amount=max_amount,minimum_quantity=minimum_quantity)       
        
            elif not product_output and  product_entry:    
                if product.amount >  int(product.maximum_amount):
                    return Response(status=status.HTTP_401_UNAUTHORIZED)  
                else: 
                    product.amount =  product.amount + int(product_entry) 
                    product.entry_quantitaty = product.entry_quantitaty + int(product_entry) 
                Log_Movimantation.objects.create(modifyer=self.request.user,description=description,code=code,type=type,cost_price=cost_price,destination=destination,status=status_product,company=company,area=area,category=category,localization=local,entry_quantitaty=product_entry,manufacturer_code=manufacturer,bar_code=code_bar,amount=product.amount,maximum_amount=max_amount,minimum_quantity=minimum_quantity)       
                    
            else:
                product.amount =  product.amount 
            product.save()
            return Response(status=status.HTTP_202_ACCEPTED)  
        else:
             return Response(status=status.HTTP_204_NO_CONTENT)

class manufacturer_view(views.APIView):
    def get_object(self,manufacturer_code):
        try:
            return Manufacturer.objects.get(manufacturer_code=manufacturer_code)
        except:
            raise Http404    
 
    def get(self,request,manufacturer_code,format=None):
        manufacturer_code = self.get_object(manufacturer_code)
        Serializer = Manufacturerserializer(manufacturer_code)
        return  Response(Serializer.data)
    
    def post(self,request,format=None):
        manufacturer_code = request.POST['manufacturer_code']
        person = request.POST['person']
        manufacturer = request.POST['manufacturer']
        fantasy = request.POST['fantasy']
        industry = request.POST['industry']
        ie_rg = request.POST['ie_rg']
        ie_indicator = request.POST['ie_indicator']
        type = request.POST['type']
        telephone1 = request.POST['telephone1']
        telephone2 = request.POST['telephone2']
        e_mail = request.POST['e_mail']
        tax_email = request.POST['tax_email']
        address_id = request.POST['address_id']
        note = request.POST['note']
        
        try:
            address = Manufacturer_address.objects.get(address_code = address_id)
        except:
            address = None
        
        Manufacturer.objects.create(manufacturer_code=manufacturer_code,person=person,manufacturer=manufacturer,fantasy=fantasy,industry=industry,ie_rg=ie_rg,ie_indicator=ie_indicator,type=type,telephone1=telephone1,note=note,telephone2=telephone2,e_mail=e_mail,tax_email=tax_email,address=address)
        return Response(status=status.HTTP_201_CREATED) 
 
    def put(self,request,format=None):
        manufacturer_code = request.POST['manufacturer_code']
        person = request.POST['person']
        manufacturer = request.POST['manufacturer']
        fantasy = request.POST['fantasy']
        industry = request.POST['industry']
        ie_rg = request.POST['ie_rg']
        ie_indicator = request.POST['ie_indicator']
        type = request.POST['type']
        telephone1 = request.POST['telephone1']
        telephone2 = request.POST['telephone2']
        e_mail = request.POST['e_mail']
        tax_email = request.POST['tax_email']
        address_id = request.POST['address_id']
        note = request.POST['note']
        try:
            address = Manufacturer_address.objects.get(address_code = address_id)
        except:
            address = None
        
        object =  Manufacturer.objects.get(manufacturer_code=manufacturer_code)
        object.person = person
        object.manufacturer=manufacturer
        object.fantasy=fantasy
        object.industry=industry
        object.ie_rg=ie_rg
        object.ie_indicator=ie_indicator
        object.type=type
        object.telephone1=telephone1
        object.note=note
        object.telephone2=telephone2
        object.e_mail=e_mail
        object.tax_email=tax_email
        object.address=address
        object.save()
        return Response(status=status.HTTP_410_GONE) 


class associated_view(views.APIView):
    def post(self,request,format=None):
        user = request.POST['user']
        code = request.POST['code']

        object  = Inputs.objects.get(code=code)
        print(object.is_used)
        if object.is_used == False:
            object.associate = user
            object.is_used = True
            object.save()   
        elif object.is_used == True:
            object.associate = ""
            object.is_used = False
            object.save()
        else:
            return Response(status=status.HTTP_423_LOCKED)    
        return Response(status=status.HTTP_202_ACCEPTED)  

class trasferir_view(views.APIView):
    def post(self,request,format=None):
        code         = request.POST['code']
        company      = request.POST['company']     
        area         = request.POST['area'] 
        try: 
            responsible  = request.POST['responsible'] 
        except: 
            responsible  = ''
         
        object  = Inputs.objects.get(code=code)
        print(object.company,object.code)
        if company == object.company  and  code ==object.code: 
            print("já existe otario")
            return Response(status=status.HTTP_208_ALREADY_REPORTED)
        # elif Inputs.objects.filter(company=company,description=object.description).exists():
        #     new_objct = Inputs.objects.get(company=company,description=object.description)
        #     new_objct.amount =  new_objct.amount + object.amount
        #     new_objct.entry_quantitaty =  new_objct.entry_quantitaty + object.amount
        #     object.active = False
        #     object.save()
        #     print("vish")
        else:
            object.company = company
            object.area = area
            object.resposible = responsible
            object.save()
            print("atualizou de boa")
        return Response(status=status.HTTP_202_ACCEPTED)   


