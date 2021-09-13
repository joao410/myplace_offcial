from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import views
from .models import Log_defect,Log_entrance,Log_association,Places,Contacts,Manufacturer,Manufacturer_address,Inputs,Stock_loc
from .serializers import Logassociationserializer,Logdefectsrializer,Logentranceserializer,Stockserializer,Inputserializer,Manufactureaddressserializer,Manufacturerserializer,Placeserializer,Contactserializer
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
       



######### API View########################

class register_product_view(views.APIView):
    def post(self,request,format=None):
        description = request.POST["description"]
        code = request.POST["code"]
        category = request.POST["category"]
        localization = request.POST["localization"]
        local =  Places.objects.get(place=localization)
        entry = datetime.today()






# class entrance_product():








######### OLD CODE ########
# @login_required(login_url='/authentication/login')  
# def category(request):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
    
#     category = Category.objects.all()
#     product = Product.objects.all()
    

#     context= {
#        'chamados_abertos':chamados_abertos,
#        'category':category,
#        'grupo' : grupo,
#        'grupos':grupos,
#        'usuarioC':usuarioC,
#        'imageP' : imageP, 
#        'product':product,
#     }
#     return render(request, 'inventory/category.html', context)   



# @login_required(login_url='/authentication/login') 
# def product(request, category_code):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
#     chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
#     product = Product.objects.filter(category_code=category_code)
#     context={
#     'chamados_abertos':chamados_abertos,    
#     "product":product,
#     'grupo' : grupo,
#     'grupos':grupos,
#     'usuarioC':usuarioC,
#     'imageP' : imageP, 
#     }

#     return render(request, 'inventory/product.html',context)   

    
# @login_required(login_url='/authentication/login') 
# def part(request, product_code):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
#     chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
#     part = Product_details.objects.filter(product_code=product_code)
#     context={
#     'chamados_abertos':chamados_abertos,    
#     "part":part,
#     'grupo' : grupo,
#     'grupos':grupos,
#     'usuarioC':usuarioC,
#     'imageP' : imageP, 
#     }

#     return render(request, 'inventory/part.html',context)   

    
# @login_required(login_url='/authentication/login') 
# def add_category(request):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
#     category = Category.objects.all()
#     product = Product.objects.all()    
#     if Log_cat_entrance.objects.all():
#             LOG_id = Log_cat_entrance.objects.all().order_by('-cat_entrance_code')[0].cat_entrance_code
                

#             cod = LOG_id + 1
#     else:
#                     cod = 100      
#     if request.method == 'POST' and 'cat_register' in request.POST:       
#         name= request.POST['category_name']
#         code = request.POST['category_code']
#         category = Category.objects.create(name=name,category_code=code)
#         category.save()
#         ########LOG#########
#         Log_cat_entrance.objects.create(cat_entrance_code=cod,category_code=category,creator=user)
#         messages.success(request, "Registrado com sucesso")
#         return redirect( 'category')

        
        
           
    
#     context= {
#        'category':category,
#        'grupo' : grupo,
#        'grupos':grupos,
#        'usuarioC':usuarioC,
#        'imageP' : imageP, 
#        'product':product,
#     }

#     return render(request, 'inventory/category.html',context)   
# @login_required(login_url='/authentication/login') 
# def add_product(request):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  

#     category = Category.objects.all()
#     product = Product.objects.all()

#     if Log_cat_entrance.objects.all():
#             LOG_id = Log_cat_entrance.objects.all().order_by('-cat_entrance_code')[0].cat_entrance_code
                

#             cod = LOG_id + 1
#     else:
#                     cod = 100        
#     if request.method == 'POST' and 'pro_register' in request.POST:       
#             brand= request.POST['brand']
#             model = request.POST['model']
#             product_code =request.POST['product_code']
#             category_code=request.POST['category_code']
#             category= Category.objects.get(category_code=category_code)
#             product = Product.objects.create(product_code=product_code,brand=brand,model=model,category_code=category)
#             product.save()
#             ########LOG#########
#             product = Product.objects.get(product_code=product_code)
#             Log_pro_entrance.objects.create(pro_entrance_code= cod, product_code=product,category_code=category,creator=user)
#             messages.success(request, "Registrado com sucesso")
#             return redirect( 'category')

#     context= {
#        'category':category,
#        'grupo' : grupo,
#        'grupos':grupos,
#        'usuarioC':usuarioC,
#        'imageP' : imageP, 
#        'product':product,
#     }

#     return render(request, 'inventory/category.html',context)   
# @login_required(login_url='/authentication/login') 
# def add_part(request):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
      
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
#     if Log_entrance.objects.all():
#             LOG_id = Log_entrance.objects.all().order_by('-entrance_code')[0].entrance_code
                

#             cod = LOG_id + 1
#     else:
#                     cod = 100  
#     if request.method == 'POST' and 'register' in request.POST:  
#         code= request.POST['part_code']
#         product = Product.objects.get(product_code=request.POST['product_code'])  
#         category = Category.objects.get(category_code= product.category_code.category_code)
#         details = request.POST['part_details'] 
#         Product_details.objects.create(part_code=code,product_code=product,details=details)
#         product.amount = product.amount + 1
#         product.save()
#         category.amount = category.amount + 1
#         category.save()
#         ########LOG#########
#         part = Product_details.objects.get(part_code=code)
#         Log_entrance.objects.create(entrance_code=cod,part_code=part,product_code=product,creator=user)
        
#         messages.success(request, "Registrado com sucesso")
#         return redirect( 'category')

        

        

#     context={
#     'grupo' : grupo,
#     'grupos':grupos,
#     'usuarioC':usuarioC,
#     'imageP' : imageP, 
  
#     }

#     return render(request, 'inventory/part.html',context)   


# @login_required(login_url='/authentication/login') 
# def part_dateils(request, part_code):
#     user = request.user   
#     usuarioC = UsuarioCorporativo.objects.get(usuario=user)
#     grupo= usuarioC.grupo
#     grupos= usuarioC.grupo.name
#     codigo = usuarioC.codigo
#     codigo = usuarioC.codigo.nome
#     imageP = ImagePerfil.objects.get(nome= codigo)
#     if not imageP.image:
#         imageP = ImagePerfil.objects.get(nome= "padrao")  
#     chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("ticket")
#     part = Product_details.objects.get(part_code=part_code)

#     try:
#         log_defect = Log_defect.objects.get(part_code = part)
#     except:
#         log_defect= "Peça em bom estado!!"
#     try:
#         part_user = UsuarioCorporativo.objects.get(usuario = part.associate)
#     except:
#         part_user = "Nenhum usuário associado!!"
#     try:
#         image_user = ImagePerfil.objects.get(nome = part_user.codigo.nome)   
#         if not image_user.image:
#             image_user = ImagePerfil.objects.get(nome = "padrao") 
#     except:
#         image_user = ImagePerfil.objects.get(nome = "padrao")   



#     context={
#     'chamados_abertos':chamados_abertos,    
#     "part":part,
#     'grupo' : grupo,
#     'grupos':grupos,
#     'usuarioC':usuarioC,
#     'imageP' : imageP, 
#     'log_defect':log_defect,
#     'part_user':part_user,
#     'image_user':image_user,
#     }

#     return render(request, 'inventory/part_dateils.html',context)   
