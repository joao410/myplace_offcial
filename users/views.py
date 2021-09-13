
from django.db.models import query
from django.db.models.expressions import CombinedExpression
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import   Department
from helpdesk.models import  Chamado,ImageLink, Chat
from .models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Companies, UsuarioPessoal,Office,Contabancaria
from files.models import  Dashbaners
from helpdesk.forms import ImageForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from helpdesk.filters import ChamadoFilter
from datetime import date, datetime
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pandas as pd
from decimal import Context, Decimal
import xlwt
from performance.forms import ImportForm
import xlrd3 as xlrd
from rest_framework import request, serializers
from rest_framework.serializers import Serializer
from  .serializers import Companies, Companyserializer, Officeserializer,WorkUserserializer,PernonalUserserializer,CorporateUserserializer,Dashbanerserializer
from rest_framework.views import APIView, Response
from rest_framework import viewsets,views,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import FileUploadParser, JSONParser
from decimal import Context, Decimal
import json
from django.http.response import JsonResponse
from django.utils.dateparse import parse_datetime
# from .form import formRegistrationAddress,formRegistrationCorporate,formRegistrationDocuments,formRegistrationPersonal,formRegistrationWork,formRegistrationBank

############ new view ############

class general_Banner_view(viewsets.ModelViewSet):
    queryset = Dashbaners.objects.filter(active=True,geral=True).order_by("order_by")
    serializer_class= Dashbanerserializer




class manager_Banner_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class=Dashbanerserializer  
    def get_queryset(self):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        list =[user.work.manager,user.user]
        query = Dashbaners.objects.filter(active=True,manager__in = list )
        return  query





class perfil_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = UsuarioCorporativo.objects.all()
    serializer_class= CorporateUserserializer
    def get_queryset(self):
        try:
            query = UsuarioCorporativo.objects.filter(user=self.request.user)
            
            return query
        except:
            raise Http404
 
class office_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Office.objects.all()
    serializer_class= Officeserializer



# class form_view(viewsets.ModelViewSet):

class user_birth(viewsets.ModelViewSet):
    serializer_class = PernonalUserserializer

    def get_queryset(self,format=None):
        data_atual = datetime.today()
        query = UsuarioPessoal.objects.filter(birthdate__month= str(data_atual.month))
        return query






class user_view(viewsets.ModelViewSet):
    serializer_class = CorporateUserserializer

    def get_queryset(self,format=None):
        
        query = UsuarioCorporativo.objects.all()
        return query


####### APIViEW ########

class user_by_idView(views.APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
           return UsuarioCorporativo.objects.get(pk= pk)
        except:
            raise Http404   
        
    def get(self,request,pk,format=None):
        pk = self.get_object(pk)
        Serializer = CorporateUserserializer(pk)
        return  Response(Serializer.data)
   


class create_user_view(views.APIView):
    
    def get(self,request,format=None):
        query ="sai"
        return Response(query)
    def post(self, request, *args, **kwargs):
        if UsuarioPessoal.objects.all():
                    Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].id

                    codigo = Usuario_id + 10001
        else:
                            codigo = 10001

        try:   
            image = request.FILES["image"]
        except:
            image = ''
        
        grupo =request.POST["group"]
        gs = Group.objects.get(name=grupo)  
    
        birthdate=request.POST["birthdate"]
        birth =   parse_datetime(birthdate)
        if not User.objects.filter(username=request.POST["user"]).exists():
                        
            if len(request.POST["password"]) < 6:
                print("muito curta safado")
              
           
            user = User.objects.create(username=request.POST["user"],email=request.POST["corporate_email"],first_name=request.POST["user"])
            user.set_password(request.POST["password"])
            user.is_active = True
            user.save()
            users = User.objects.get(username=request.POST["user"])

            try:
                UsuarioPessoal.objects.create(code=codigo,
                name=request.POST.get("name",""),
                gender=request.POST.get("gender",""),
                surname=request.POST.get("surname",""),
                personal_cell=request.POST.get("personal_cell",""),
                cpf=request.POST.get("cpf",""),
                color=request.POST.get("color",""),
                marital_status=request.POST.get("marital_status",""),
                schooling=request.POST.get("schooling",""),
                pis=request.POST.get("pis",""),
                voter_title=request.POST.get("voter_title",""),
                work_card= request.POST.get("work_card",""),
                series=request.POST.get("series",""),
                work_card_uf=request.POST.get("work_card_uf",""),
                work_card_date=request.POST.get("work_card_date",""),
                birthdate=birth,
                birthdate_uf=request.POST.get("birthdate_uf",""),
                city_birth=request.POST.get("city_birth",""),
                country_birth=request.POST.get("country_birth",""),
                national_country= request.POST.get("national_country",""),
                mother=request.POST.get("mother",""),
                father=request.POST.get("father",""),
                profile_image=image)               
            except:
                UsuarioPessoal.objects.create(code=codigo,
                name=request.POST.get("name",""),
                gender=request.POST.get("gender",""),
                surname=request.POST.get("surname",""),
                personal_cell=request.POST.get("personal_cell",""),
                cpf=request.POST.get("cpf",""),
                color=request.POST.get("color",""),
                marital_status=request.POST.get("marital_status",""),
                schooling=request.POST.get("schooling",""),
                pis=request.POST.get("pis",""),
                voter_title=request.POST.get("voter_title",""),
                work_card= request.POST.get("work_card",""),
                series=request.POST.get("series",""),
                work_card_uf=request.POST.get("work_card_uf",""),
                birthdate=request.POST.get("birthdate",""),
                birthdate_uf=request.POST.get("birthdate_uf",""),
                city_birth=request.POST.get("city_birth",""),
                country_birth=request.POST.get("country_birth",""),
                national_country= request.POST.get("national_country",""),
                mother=request.POST.get("mother",""),
                father=request.POST.get("father",""),
                profile_image=image)               
            u = UsuarioPessoal.objects.get(name=request.POST.get("name",""))
            office = Office.objects.get(office=request.POST.get("office",""))
            try:
                usua= UsuarioTrabalho.objects.create(code=u,department=request.POST.get("department","") ,company=request.POST.get("company",""),office=office,transport_voucher=request.POST.get("transport_voucher",""),admission_date=request.POST.get("admission_date",""),resignation_date=request.POST.get("resignation_date",""),admission_type= request.POST.get("admission_indicative",""),first_job= request.POST.get("first_job",""),work_regime=request.POST.get("work_regime",""),pension_scheme= request.POST.get("pension_scheme",""),day_regime= request.POST.get("day_regime",""),nature_activity=request.POST.get("nature_activity",""),category=request.POST.get("category",""),function_code=request.POST.get("function_code",""),workload=request.POST.get("workload",""),wage_unit=request.POST.get("wage_unit",""),variable_salary=request.POST.get('variable_salary', 0.00 ),note=request.POST.get("note",""))
                t = UsuarioTrabalho.objects.get(codigo=u)
            except:
                usua= UsuarioTrabalho.objects.create(code=u,department=request.POST.get("department","") ,company=request.POST.get("company",""),office=office)
                t = UsuarioTrabalho.objects.get(codigo=u)
            try:
                do= UsuarioDocumentos.objects.create(code=u,document=request.POST.get("document",""),document_number=request.POST.get("document_number",""),organ=request.POST.get("organ",""),dispatch_date=request.POST.get("dispatch_date",""),shelf_life=request.POST.get("shelf_life",""))              
                d =  UsuarioDocumentos.objects.get(codigo=u)  
            except:
                do= UsuarioDocumentos.objects.create(code=u)  
                d =  UsuarioDocumentos.objects.get(codigo=u)               
            try:
                en=UsuarioEndereco.objects.create(code=u,zip_code=request.POST.get("zip_code",""),type=request.POST.get("type",""),public_place= request.POST.get("public_place",""),number=request.POST.get("number",""),uf=request.POST.get("uf",""),city=request.POST.get("city",""),district=request.POST.get("district",""),complement=request.POST.get("complement",""),country=request.POST.get("country",""))
                e = UsuarioEndereco.objects.get(codigo=u)
            except:
                en=UsuarioEndereco.objects.create(code=u)
                e = UsuarioEndereco.objects.get(codigo=u)
            try:
                co = Contabancaria.objects.create(code=u,bank=request.POST.get("bank",""),account=request.POST.get("account",""),agency=request.POST.get("agency",""))    
            except:
                pass
            try:    
                usuar  = UsuarioCorporativo.objects.create(code=u,work=usua,document=do,address=en,user=users,group=gs,corporate_email=request.POST.get("corporate_email",""),skype=request.POST.get("skype",""),corporate_phone= request.POST.get("corporate_phone",""),telephone=  request.POST.get("telephone",""),ramal=request.POST.get("ramal",""),bank=co)
            except:
                 usuar  = UsuarioCorporativo.objects.create(code=u,user=users,group=gs,corporate_email=request.POST.get("corporate_email",""),skype=request.POST.get("skype",""),corporate_phone= request.POST.get("corporate_phone",""),telephone=  request.POST.get("telephone",""),ramal=request.POST.get("ramal",""),bank=co)  
            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            raise Http404             







class create_banner_view(views.APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self,request,format=None):
        image = request.FILES["bannerimage"]
        description = request.POST["description"]
        order = request.POST["order"]
        general = request.POST["general"]
        time = request.POST["time"]
        try:
            gestor = request.POST["gestor"]
        except:
            gestor = ""
        if general == True:
            if Dashbaners.objects.filter(order_by=order,geral=True).exists():
                bans= Dashbaners.objects.filter(geral=True,order_by__gte = order).order_by('order_by')
                for ban in bans:
                    ban.order_by = ban.order_by + 1
                    ban.save()
                Dashbaners.objects.create(image=image,desc=description,manager=gestor,geral=general,order_by = order,timeshow=time)    
            else:
                Dashbaners.objects.create(image=image,desc=description,manager=gestor,geral=general,order_by = order,timeshow=time)
        else:
            if Dashbaners.objects.filter(order_by=order,manager=gestor).exists():
                bans= Dashbaners.objects.filter(manager=gestor,order_by__gte = order).order_by('order_by')
                for ban in bans:
                    ban.order_by = ban.order_by + 1
                    ban.save()
                Dashbaners.objects.create(image=image,desc=description,manager=gestor,geral=general,order_by = order,timeshow=time)        
            else:
                Dashbaners.objects.create(image=image,desc=description,manager=gestor,geral=general,order_by = order,timeshow=time)

        return Response(status=status.HTTP_201_CREATED)



class modify_banner_view(views.APIView):
    # permission_classes = (IsAuthenticated,)
    def put(self,request,format=None):
        banner = Dashbaners.objects.get(pk=request.POST["pk"])
        if banner.active == True:
            banner.active = False
            banner.save()  
            return Response(status=status.HTTP_202_ACCEPTED)          
        else:
            banner.active = True
            banner.save()
            return Response(status=status.HTTP_202_ACCEPTED)          
        
        






















########## old view ######### 

today = date.today()

# Create your views here.

@login_required(login_url='/authentication/login')    
def add_usuarios(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(user=user)
    g = Group.objects.all()
    grupo= usuarioC.grupo
    departamento = Department.objects.all().order_by("name")
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome   

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,
    'g':g,  
    'grupo':grupo,
  
    'admin':admin, 
    'filtro': filtro,

 
    'form':ImageForm,
    'departamento':departamento,
    
            }  
    if UsuarioPessoal.objects.all():
            Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].id
                

            codigo = Usuario_id + 10001
    else:
                    codigo = 10001
                                
    if request.method == 'POST' and 'add_usu' in request.POST:  
        
        #pessoal#
        try :
            nome = request.POST["nome"]
            nome = nome.upper()
            apelido = request.POST["apelido"]
            cpf = request.POST["cpf"]
            genero = request.POST["genero"]
            cor = request.POST["cor"]
            ecivil = request.POST["ecivil"]
            escolaridade = request.POST["escolaridade"]
            datanasci = request.POST["datanasci"]
            municipionasc = request.POST["municipionasc"]
            ufnasci = request.POST["ufnasci"]
            paisnasci = request.POST["paisnasci"]
            nasciona = request.POST["nasciona"]
            mae = request.POST["mae"]
            pai = request.POST["pai"]
            pis = request.POST["pis"]
            teleitor =  request.POST["titulo"]
            ctrabalho = request.POST["carteira"]       
            serie = request.POST["serie"]
            uf = request.POST["ufc"]
            emissao = request.POST["emissao"]
            celp = request.POST["celp"]
        except:
            pass    
        #trabalho# 
        try:
            emp = request.POST["empresa"]
            dep = request.POST["departamento"]       
            cargo = request.POST["cargo"]
            vtrans = request.POST["vtrans"]
            admissao = request.POST["admissao"]
            demissao = request.POST["demissao"]
            tipo = request.POST["tipoadmissao"]
            indica =  request.POST["indica"]
            priempr = request.POST["priempr"]
            rtrab = request.POST["rtrab"]
            rprev = request.POST["rprev"]
            rjorn = request.POST["rjorn"]
            naativ = request.POST["naativ"]
            cat = request.POST["cat"]
            codf = request.POST["codf"]
            carh = request.POST["carh"]
            unisa = request.POST["unisa"]
            obs = request.POST["obs"]
            salvari = request.POST["salvari"]
            if not salvari:
                salvari =0.00
        except:
            pass
        #conta#
        try:
            banco = request.POST["banco"]
            agencia = request.POST["agencia"]
            conta = request.POST["conta"]
        except:
            pass    
        #documento#
        try:
            documento = request.POST["documento"]
            ndocumento = request.POST["numero"]
            oe = request.POST["oe"]
            de = request.POST["expedicao"]
            validade = request.POST["validade"]
        except:
            pass     
        #endereço#
        try:
            cep = request.POST["cep"]
            tipo = request.POST["tipo"]
            num = request.POST["num"]
            ufatual = request.POST["ufatual"]
            muniatual = request.POST["muniatual"]
            bairro = request.POST["bairro"]
            logradouro = request.POST["logradouro"]
            complemento = request.POST["complemeno"]
            pais = request.POST["pais"]
        except:
            pass
        #corporativo#
        try:
            email1 = request.POST["email1"]       
            email2 = request.POST["email2"]       
            skype = request.POST["skype"]       
            cel = request.POST["cel"]       
            tel = request.POST["tel"]       
            ramal = request.POST["ramal"]       
            usuario = request.POST["usuario"] 
            usuario = usuario.upper()      
            senha = request.POST["senha"]  
            senha=senha.upper() 
            repassword = request.POST["senha"]    
            repassword = repassword.upper()
            
            grupo = request.POST["grupo"] 
            gs = Group.objects.get(name=grupo)   
        except:
            pass
        if vtrans == "SIM":
           vtrans =  "VALE TRANSPORTE"
        if vtrans == "NÃo":
           vtrans =  "AJUDA DE CUSTO"  
        if not vtrans:  
           vtrans = "---"            
    
                  
        if not User.objects.filter(username=usuario).exists():
                        
            if len(senha) < 6:
                messages.error(request, "Senha muito curta(<6)")
                return render(request, 'users/add_usuarios.html', context)
            
            if senha != repassword:
                messages.error(request, "As senhas nao batem")
                return render(request, 'users/add_usuarios.html', context)
            user = User.objects.create(username=usuario,email=email1,first_name=usuario)
            user.set_password(senha)
            user.is_active = True
            user.save()
            users = User.objects.get(username=usuario)
            try:
                UsuarioPessoal.objects.create(codigo=codigo,nome=nome,genero=genero,apelido=apelido,celpessoal=celp,cpf=cpf,cor=cor,ecivil=ecivil,escolaridade=escolaridade,pis=pis,tituloeleitor=teleitor,carteiratrabalho=ctrabalho,serie=serie,ufcarteiratrabalho=uf,datacarteiratrabalho=emissao,datanacimento=datanasci,ufnacimento=ufnasci,municipionacimento=municipionasc,paisnacimento=paisnasci,paisnacionalidade=nasciona,nomemae=mae,nomepai=pai)
            except:
                UsuarioPessoal.objects.create(codigo=codigo,nome=nome,genero=genero,apelido=apelido,cpf=cpf,celpessoal=celp,cor=cor,ecivil=ecivil,escolaridade=escolaridade,pis=pis,tituloeleitor=teleitor,carteiratrabalho=ctrabalho,serie=serie,ufcarteiratrabalho=uf,datanacimento=datanasci,ufnacimento=ufnasci,municipionacimento=municipionasc,paisnacimento=paisnasci,paisnacionalidade=nasciona,nomemae=mae,nomepai=pai)
            u = UsuarioPessoal.objects.get(nome=nome)
            c= Office.objects.get(cargo=cargo)
            try:
                usua = UsuarioTrabalho.objects.create(codigo=u,departamento=dep,empresa=emp,cargo=c,valetransporte=vtrans,dataadmissao=admissao,datademissao=demissao,indicativoadmissao=indica,primeiroemprego=priempr,regimetrabalho=rtrab,regimeprevidenciario=rprev,regimejornada=rjorn,naturezaatividade=naativ,categoria=cat,codigofuncao=codf,cargahorariam=carh,unidadesalarial=unisa,salariovariavel=salvari,obs=obs)
                t = UsuarioTrabalho.objects.get(codigo=u)
            except:
                pass    
            try:
                do = UsuarioDocumentos.objects.create(codigo=u,documento=documento,numerodocumento=ndocumento,orgao=oe,dataexpedissao=de,validade=validade)
                d =  UsuarioDocumentos.objects.get(codigo=u)
            except:
                pass    
            try:
                en = UsuarioEndereco.objects.create(codigo=u, cep=cep,tipo=tipo,logradouro=logradouro,numero=num,ufatual=ufatual,municipioatul=muniatual,bairroatual=bairro,complemento=complemento,pais=pais)
                e = UsuarioEndereco.objects.get(codigo=u)
            except:
                pass    
            try:
                co = Contabancaria.objects.create(codigo=u,banco=banco,conta=conta,agencia=agencia)
            except:
                pass
            try:    
                usuar  = UsuarioCorporativo.objects.create(codigo=u,trabalho=t,documento=d,endereco=e,email=email1,emailCorporativo=email2,skype=skype,telefone=cel,tel=tel,ramal=ramal,usuario=users,grupo=gs,banco=co)
            except:
                 usuar  = UsuarioCorporativo.objects.create(codigo=u,email=email1,emailCorporativo=email2,skype=skype,telefone=cel,tel=tel,ramal=ramal,usuario=users,grupo=gs)
            
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                nome = request.POST['usuario']
                img = form.cleaned_data.get("imagem") 
                obs=''
                users = User.objects.get(username=usuario)
                usuari = UsuarioCorporativo.objects.get(usuario=users)
                us = usuari.codigo.nome

                        
                obj =ImagePerfil.objects.create(image=img,obs=obs,nome=us)
                obj.save()
                messages.success(request, 'Imagem adicionada')    
            else:
                messages.error(request, 'Imagem não adicionada')
            messages.success(request, "Usuario criado com sucesso")
            return redirect( 'presidente')
        elif User.objects.filter(username=usuario).exists and UsuarioCorporativo.objects.filter(usuario=user).exists:
              messages.error(request, 'Usuario existente')
        else:
                users = User.objects.get(username=usuario)
                usu = UsuarioCorporativo.objects.create(name=nome,empresa=emp, departamento=dep,cargo=cargo,email=email1,email_corporativo=email2,skype=skype,telefone=cel,tel=tel,ramal=ramal,usuario=users,password=senha,grupo=gs)
                usu.save()
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    nome = request.POST['usuario']
                    img = form.cleaned_data.get("imagem") 
                    obs=''
                    users = User.objects.get(username=usuario)
                    usuari = UsuarioCorporativo.objects.get(usuario=users)
                    obj =ImagePerfil.objects.create(usuario=usuari,image=img,obs=obs,nome=nome)
                    obj.save()
                    messages.success(request, 'Imagem adicionada')
               

                
    return render(request, 'users/add_usuarios.html', context)        
    
    
@login_required(login_url='/authentication/login')    
def edit_usuarios(request,id):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    g = Group.objects.all()
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    empresa = Empresa.objects.all()
    departamento = Departamento.objects.all().order_by("name")
    cargos = Cargo.objects.all().order_by("cargo")
    filtro = ChamadoFilter()
    usu = UsuarioCorporativo.objects.get(pk=id)
    cod =usu.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")
    image = ImagePerfil.objects.get(nome=cod)
    if not image.image:
      image = ImagePerfil.objects.get(nome= "padrao")

    if request.method == 'POST' and 'next' in request.POST:
        id = usu.id + 1
        try:
            usu = UsuarioCorporativo.objects.get(pk=id)
            usup = UsuarioPessoal.objects.get(codigo= usu.codigo.codigo)
           
            usue = UsuarioEndereco.objects.get(codigo=usu.codigo)
            cod =usu.codigo.nome
            imageP = ImagePerfil.objects.get(nome= codigo)
            if not imageP.image:
                imageP = ImagePerfil.objects.get(nome= "padrao")
            image = ImagePerfil.objects.get(nome=cod)
            if not image.image:
                image = ImagePerfil.objects.get(nome= "padrao")
        
        except:
            try:
                us = UsuarioCorporativo.objects.all().last()
                i= us.id
                while id > 0 and id <= i:
                    try:
                        id = id+1  
                        usu = UsuarioCorporativo.objects.get(pk=id)
                       
                        cod =usu.codigo.nome
                        imageP = ImagePerfil.objects.get(nome= codigo)
                        if not imageP.image:
                            imageP = ImagePerfil.objects.get(nome= "padrao")
                        image = ImagePerfil.objects.get(nome=cod)
                        if not image.image:
                            image = ImagePerfil.objects.get(nome= "padrao")
                        break   
                    except:
                        pass 
            except:
                pass
    if request.method == 'POST' and 'previos' in request.POST:
        id = usu.id -1
        try:
            usu = UsuarioCorporativo.objects.get(pk=id)
           
            cod =usu.codigo.nome
            imageP = ImagePerfil.objects.get(nome= codigo)
            if not imageP.image:
                imageP = ImagePerfil.objects.get(nome= "padrao")
            image = ImagePerfil.objects.get(nome=cod)
            if not image.image:
                image = ImagePerfil.objects.get(nome= "padrao")
        except:
           while id >0: 
                id = id-1  
                try:
                    usu = UsuarioCorporativo.objects.get(pk=id)
                   
                    cod =usu.codigo.nome
                    imageP = ImagePerfil.objects.get(nome= codigo)
                    if not imageP.image:
                        imageP = ImagePerfil.objects.get(nome= "padrao")
                    image = ImagePerfil.objects.get(nome=cod)
                    if not image.image:
                        image = ImagePerfil.objects.get(nome= "padrao")
                    break    
                except:
                    pass
   
    if request.method == 'POST' and 'edit_usu' in request.POST:  
        nome = request.POST["nome"]
        apelido = request.POST["apelido"]
        cpf = request.POST["cpf"]
        genero = request.POST["genero"]
        cor = request.POST["cor"]
        ecivil = request.POST["ecivil"]
        escolaridade = request.POST["escolaridade"]
        datanasci = request.POST["datanasci"]
        municipionasc = request.POST["municipionasc"]
        ufnasci = request.POST["ufnasci"]
        paisnasci = request.POST["paisnasci"]
        nasciona = request.POST["nasciona"]
        mae = request.POST["mae"]
        pai = request.POST["pai"]
        pis = request.POST["pis"]
        teleitor =  request.POST["titulo"]
        ctrabalho = request.POST["carteira"]       
        serie = request.POST["serie"]
        uf = request.POST["ufc"]
        emissao = request.POST["emissao"]
        celp = request.POST["celp"]
        #trabalho# 
        
        emp = request.POST["empresa"]
        dep = request.POST["departamento"]       
        cargo = request.POST["cargo"]
        vtrans = request.POST["vtrans"]
        admissao = request.POST["admissao"]
        demissao = request.POST["demissao"]
        tipo = request.POST["tipoadmissao"]
        indica =  request.POST["indica"]
        priempr = request.POST["priempr"]
        rtrab = request.POST["rtrab"]
        rprev = request.POST["rprev"]
        rjorn = request.POST["rjorn"]
        naativ = request.POST["naativ"]
        cat = request.POST["cat"]
        codf = request.POST["codf"]
        carh = request.POST["carh"]
        unisa = request.POST["unisa"]
        obs = request.POST["obs"]
        salvari = request.POST["salvari"]
        #conta#
        banco = request.POST["banco"]
        agencia = request.POST["agencia"]
        conta = request.POST["conta"]
        #documento#
        documento = request.POST["documento"]
        ndocumento = request.POST["numero"]
        oe = request.POST["oe"]
        de = request.POST["expedicao"]
        validade = request.POST["validade"]
        #endereço#
        cep = request.POST["cep"]
        tipoe = request.POST["tipo"]
        num = request.POST["num"]
        ufatual = request.POST["ufatual"]
        muniatual = request.POST["muniatual"]
        bairro = request.POST["bairro"]
        logradouro = request.POST["logradouro"]
        complemento = request.POST["complemeno"]
        pais = request.POST["pais"]
        #corporativo#
        email1 = request.POST["email1"]       
        email2 = request.POST["email2"]       
        skype = request.POST["skype"]       
        cel = request.POST["cel"]       
        tel = request.POST["tel"]       
        ramal = request.POST["ramal"]       
        usuario = request.POST["usuario"]       
        
        grupo = request.POST["grupo"] 
  
        gs = Group.objects.get(name=grupo)  
        
        if vtrans == "SIM":
           vtrans =  "VALE TRANSPORTE"
        if vtrans == "NÃo":
           vtrans =  "AJUDA DE CUSTO"  
        if vtrans == "None":  
            vtrans = "---"     
        if priempr == "None":  
            priempr = "---"     

        if  User.objects.filter(username=usuario).exists():             
            usern = User.objects.get(username=usuario)
            usern.is_active = True
            usern.save()
            users = User.objects.get(username=usuario)
            usup = UsuarioPessoal.objects.get(codigo= usu.codigo.codigo)
            usup.nome = nome
            usup.apelido= apelido
            usup.cpf = cpf
            usup.pis = pis
            usup.tituloeleitor = teleitor
            usup.carteiratrabalho = ctrabalho
            usup.serie = serie
            usup.ufcarteiratrabalho = uf
            try:
                usup.datacarteiratrabalho = datetime.strptime(de,'%d/%m/%Y')
            except:
                usup.datacarteiratrabalho = None      
            usup.genero = genero
            usup.cor = cor
            usup.ecivil= ecivil
            usup.celpessoal= celp
            usup.escolaridade  = escolaridade
            usup.datanacimento = datetime.strptime(datanasci ,'%d/%m/%Y')
            usup.ufnacimento = ufnasci
            usup.municipionacimento = municipionasc
            usup.paisnacimento = paisnasci
            usup.paisnacionalidade = nasciona
            usup.nomemae = mae
            usup.nomepai = pai
            usup.save()
            try: 
                    contas = Contabancaria.objects.get(codigo=usu.codigo)
                    contas.banco = banco
                    contas.agencia = agencia
                    contas.conta = conta
                    contas.save()
            except:
                    u=UsuarioPessoal.objects.get(pk=usup.id)
                    contab = Contabancaria.objects.create(codigo=u,banco=banco,agencia=agencia,conta=conta)
                    contab.save()
                    usu.banco = contab
                    usu.save
            if UsuarioTrabalho.objects.filter(codigo=usu.codigo).exists():    
                    usut = UsuarioTrabalho.objects.get(codigo=usu.codigo)
                    usut.empresa = emp
                    usut.departamento = dep
                    usut.cargo = Cargo.objects.get(cargo=cargo)
                
                    usut.valetransporte = vtrans
                    
                    try:
                        usut.dataadmissao = datetime.strptime(admissao,'%d/%m/%Y')
                    except:
                        usut.dataadmissao = None
                    try:   
                        usut.datademissao = datetime.strptime(demissao,'%d/%m/%Y')
                    except:
                        usut.datademissao = None
                    usut.tipoAdmissao = tipo
                    usut.indicativoadmissao= indica
                    usut.primeiroemprego = priempr
                    usut.regimetrabalho = rtrab
                    usut.regimeprevidenciario = rprev
                    usut.regimejornada = rjorn
                    usut.naturezaatividade = naativ
                    usut.categoria = cat
                    usut.codigofuncao = codf
                    usut.cargahorariam = carh
                    usut.unidadesalarial = unisa
                    try:
                        usut.salariovariavel = Decimal(salvari.replace(',','.'))
                    except :
                        usut.salariovariavel = 0
                    usut.obs = obs
                    usut.save()
            else:   
                    c =Cargo.objects.get(cargo=cargo)
                    u=UsuarioPessoal.objects.get(pk=usup.id)
                    trab = UsuarioTrabalho.objects.create(codigo=u,cargo=c)
                    trab.save()
                    usu.trabalho = trab
                    usu.save()
            try:
                if UsuarioDocumentos.objects.filter(codigo=usu.codigo).exists():
                        usud = UsuarioDocumentos.objects.get(codigo=usu.codigo)  
                        usud.documento= documento
                        usud.numerodocumento = ndocumento
                        usud.orgao = oe
                        try:
                            usud.dataexpedissao =  datetime.strptime(de,'%d/%m/%Y')
                        except:
                            usud.dataexpedissao = None
                        try:
                            usud.validade =  datetime.strptime(validade,'%d/%m/%Y')
                        except:
                            usud.validade = None
                        usud.save()
                else:  
                
                        u=UsuarioPessoal.objects.get(pk=usup.id)
                        do = UsuarioDocumentos.objects.create(codigo=u,documento=documento,numerodocumento=ndocumento,orgao=oe,dataexpedissao=de,validade=validade)
                        do.save()
                        usu.documento = do
                        usu.save()
            except:      
                u=UsuarioPessoal.objects.get(pk=usup.id)
                doc = UsuarioDocumentos.objects.create(codigo=u)
                doc.save()
                usu.documento = doc
                usu.save()   
            if UsuarioEndereco.objects.filter(codigo=usu.codigo).exists():  
                    usue = UsuarioEndereco.objects.get(codigo=usu.codigo)
                    usue.cep = cep
                    usue.tipo = tipoe
                    usue.logradouro = logradouro
                    usue.numero = num
                    usue.ufatual = ufatual
                    usue.MunicipioAtul = muniatual
                    usue.bairroatual = bairro
                    usue.complemento = complemento
                    usue.pais = pais
                    usue.save() 

            else:
            
                    u=UsuarioPessoal.objects.get(pk=usup.id)
                    en = UsuarioEndereco.objects.create(codigo=u, cep=cep,tipo=tipo,logradouro=logradouro,numero=num,ufatual=ufatual,municipioatul=muniatual,bairroatual=bairro,complemento=complemento,pais=pais)
                    en.save()
                    usu.endereco = en
                    usu.save()
                   
            usu.email = email1
            usu.emailCorporativo = email2
            usu.skype = skype
            usu.telefone = cel
            usu.tel = tel
            usu.ramal = ramal
            usu.usuario = users
            usu.grupo= gs
            usu.save()
            try:
                form = ImageForm(request.POST, request.FILES)
                imageu = ImagePerfil.objects.get(nome = cod)
                imageu.nome = usup.nome
                imageu.image =  form.cleaned_data.get("imagem")  
                imageu.save() 
                messages.success(request, "Usuario editado  com sucesso")
            except:
                pass
    

    if request.method == 'POST' and 'exc_usu' in request.POST: 
        id = request.POST['exc_usu']
        usuario= UsuarioCorporativo.objects.get(pk=id)
        usuario.delete()
        return redirect( 'presidente')         
    context = {
        'chamados': chamados,
        'chamados_abertos': chamados_abertos,
        'grupos': grupos,
        'usuarioC':usuarioC,
        'user' : user,
        'g':g,  
        'grupo':grupo,
        'admin':admin, 
        'filtro': filtro,
        'imageP':imageP,   
        'form':ImageForm,
        'usu': usu,
        'image':image,
        'empresa':empresa,
        'cargos':cargos, 
        'departamento':departamento,
            }              
    return render(request, 'users/edit_usuarios.html', context)        
@login_required(login_url='/authentication/login')    
def perfis(request):
    ids = request.POST["perfil"]
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    usuario = UsuarioCorporativo.objects.get(pk=ids)
    grupo= usuarioC.grupo
    codigo = usuarioC.codigo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome= codigo.nome)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")
    img = ImagePerfil.objects.get(nome=usuario.codigo.nome)
    if not img.image:
      img = ImagePerfil.objects.get(nome= "padrao")
    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,   
    'img':img, 
    'usuario':usuario,
            }  
    return render(request, 'users/perfis.html', context)        
    
@login_required(login_url='/authentication/login')    
def perfisuser(request):
    ids = request.POST["perfil"]
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    usuario = UsuarioCorporativo.objects.get(pk=ids)
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    cod =usuario.codigo.nome
    
    try:
        image = ImagePerfil.objects.get(nome=cod)
        if not image.image:
            image = ImagePerfil.objects.get(nome="padrao")
    except:
        image = ImagePerfil.objects.get(nome= "padrao") 
    imageP = ImagePerfil.objects.get(nome=codigo) 
    try:
        imageP = ImagePerfil.objects.get(nome= codigo.nome)
        if not imageP.image:
            imageP = ImagePerfil.objects.get(nome= "padrao")
    except:
        imageP = ImagePerfil.objects.get(nome= "padrao")
    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,
    'image':image, 
    'usuario':usuario,
            }  
   
        
               
    return render(request, 'users/perfisuser.html', context)      
@login_required(login_url='/authentication/login')    
def home(request):
    user = request.user
    admin = Chamado.objects.all()
          
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    codigo = usuarioC.codigo
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name

    filtro = ChamadoFilter()
    try:
        imageP = ImagePerfil.objects.get(nome= codigo.nome)
        if not imageP.image:
            imageP = ImagePerfil.objects.get(nome= "padrao")
    except:
        imageP = ImagePerfil.objects.get(nome= "padrao")          
      
    
       
    

 
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user, 
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP,    
            }  

    if request.method == 'POST' and 'salvar' in request.POST:
        
        nome = request.POST["name"]
        problema = request.POST["problem"]
        urgencia = request.POST["urgency"]
        if not nome:
                messages.error(
                    request, "Por favor preencha os campos ")
                return render(request, 'home/home.html', context)

        if not problema:
                messages.error(request, "Por favor escolha um assunto para tratar")
                return render(request, 'home/home.html', context)
        if not urgencia:
                messages.error(request, "Por favor escolha a urgencia do assunto")
                return render(request, 'home/home.html', context)        
        Chamado.objects.create(username=nome, problem=problema, urgency=urgencia)
        messages.success(request, 'Chamado criado com sucesso')



    return render(request, 'users/home.html', context) 
@login_required(login_url='/authentication/login')  
def presidente(request):
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    users = UsuarioCorporativo.objects.all().order_by("codigo")
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    codigo = usuarioC.codigo.nome
    imageP = ImagePerfil.objects.get(nome= codigo)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")

    filtro = ChamadoFilter()
    context = {
    'chamados': chamados,
    'chamados_abertos': chamados_abertos,
    'grupos': grupos,
    'usuarioC':usuarioC,
    'user' : user,  
    'users' : users,  
    'grupo':grupo,
    'admin':admin, 
    'filtro': filtro,
    'imageP':imageP, 
    'form':ImportForm(),   
            }  
    if request.method == 'GET':
        myFilter = ChamadoFilter(request.GET, queryset=users)
        users = myFilter.qs
               
        user = request.user
        users = UsuarioCorporativo.objects.all().order_by("codigo")
        grupo= usuarioC.grupo
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        grupos= usuarioC.grupo.name

        context = {
            'users':users,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,   
            'form':ImportForm(),                   
                }  
    
    if request.method == 'POST' and 'btn_import' in request.POST:
        input_excel = request.FILES['file']
        workbook =xlrd.open_workbook(file_contents=input_excel.read())
        sheet = workbook.sheet_by_index(0)
       

        erro_list = list()
        a =1
       
        for sheet.nrows in range(sheet.nrows):
            try:
                nome = sheet.cell_value(a,0)
                nome = nome.upper()
                cargo = sheet.cell_value(a,1)
                cpf = sheet.cell_value(a,2)
                datanasci = sheet.cell_value(a,3)
                usuario =sheet.cell_value(a,4) 
                usuario = usuario.upper()      
                senha = sheet.cell_value(a,5) 
                repassword = sheet.cell_value(a,5)    
                grupo = sheet.cell_value(a,6) 
                gs = Group.objects.get(name=grupo)   
            except:
                pass
            
            if UsuarioPessoal.objects.all():
                Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].id
                

                codigo = Usuario_id + 10001
            else:
                    codigo = 10001
            
            try :
                usern = User.objects.values().get(username=usuario)
                erro_list.append(usern)
                test_erro = True
                obj =ImagePerfil.objects.create(nome=nome)
                obj.save()
                        
            except:
                usern = User.objects.create(username=str(usuario),first_name=str(usuario))
                usern.set_password(int(senha))
                usern.is_active = True
                usern.group = str(gs)
                usern.save()
               
                up= UsuarioPessoal.objects.create(codigo=codigo,nome=nome,cpf=cpf)
                up.save()
                u = UsuarioPessoal.objects.get(codigo=codigo)
                us = u.codigo
                try:
                    c= Cargo.objects.get(cargo=cargo)
                    ta= UsuarioTrabalho.objects.create(codigo=us,cargo=c)
                    ta.save()
                except:
                    pass     
                try:
                    t = UsuarioTrabalho.objects.get(codigo=us)
                except:
                    pass    
                try:
                    uc = UsuarioCorporativo.objects.create(codigo=u,trabalho=t,usuario=usern,grupo=gs)   
                    uc.save()
                except:
                    uc = UsuarioCorporativo.objects.create(codigo=u,usuario=usern,grupo=gs) 
                    uc.save()  
                obj =ImagePerfil.objects.create(nome=nome)
                obj.save()     

            a = a+1     
                        
        context = {
            'form':ImportForm(),
            
            'test_erro':test_erro,
            'erro_list':erro_list,
            'form_image':ImageForm,
            'chamados': chamados,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            'user': request.user,
            'users' : users,  
            'grupo':grupo,
            'admin':admin, 
            'filtro': filtro,
            'imageP':imageP, 
            'form':ImportForm(),   
        }

        return render(request, 'users/presidente.html', context)                
    return render(request, 'users/presidente.html', context)     

MDATA = datetime.now().strftime('%d-%m-%Y')
def export_xlsx(model, filename, queryset, columns):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(model)
    ws.col(0).width = 256 * 30
    ws.col(1).width = 256 * 30
    ws.col(2).width = 200 * 30
    ws.col(3).width = 200 * 30
    ws.col(4).width = 200 * 30
    
   
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    default_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    rows = queryset
    for row, rowdata in enumerate(rows):
        row_num += 1
        for col, val in enumerate(rowdata):
            ws.write(row_num, col, val, default_style)

    wb.save(response)
    return response
def exportar_colaboradores(request):
    MDATA = datetime.now().strftime('%Y-%m-%d')
    model = 'Users'
    filename = 'colaboradores_exportados.xls'
    _filename = filename.split('.')
    filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
    queryset = UsuarioCorporativo.objects.all().order_by("codigo__nome").values_list(
        'codigo__nome',
        'trabalho__cargo__cargo',
        'trabalho__departamento',
        'trabalho__dataadmissao',
        'codigo__datanacimento',
    )
    columns = ('Nome', 'Cargo','Departamento','Admissão','Data Nascimento')
    response = export_xlsx(model, filename_final, queryset,columns)
    return response

@login_required(login_url='/authentication/login')    
def problem(request): 
    user = request.user
    admin = Chamado.objects.all()        
    usuarioC = UsuarioCorporativo.objects.get(usuario=user)
    users = UsuarioCorporativo.objects.all()
    codigo = usuarioC.codigo
   
    grupo= usuarioC.grupo
    chamados = Chamado.objects.filter(grupo=grupo).order_by("-id")    
    chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("-id")
    grupos= usuarioC.grupo.name
    imageP = ImagePerfil.objects.get(nome= codigo.nome)
    if not imageP.image:
      imageP = ImagePerfil.objects.get(nome= "padrao")

    filtro = ChamadoFilter()
    context = {
            'chamados': chamados,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'user' : user, 
            'users' : users,
            'usuarioC':usuarioC,
            
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }       
    if request.method == 'GET':
        myFilter = ChamadoFilter(request.GET, queryset=users)
        users = myFilter.qs 
        user = request.user
        usuarioC = UsuarioCorporativo.objects.get(usuario=user)
        grupo= usuarioC.grupo
        chamados_abertos = Chamado.objects.filter(active=True,grupo=grupo).order_by("id")
        grupo= usuarioC.grupo.name

        context = {
            'users':users,
            'chamados_abertos': chamados_abertos,
            'grupos': grupos,
            'usuarioC':usuarioC,
            
            'user' : user,  
            'grupo':grupo,
            'filtro': filtro,  
            'imageP':imageP,                   
                }            
    return render(request, 'users/problem.html', context)

@login_required(login_url='/authentication/login')    
def cargo(request):
    if request.method == 'POST' and 'cargo' in request.POST:
        cargo = request.POST["cargo"]
        ncbo = request.POST["ncbo"]
        Cargo.objects.create(cargo=cargo,ncbo=ncbo)
        messages.success(request,'Cadastrado com sucesso')
    return redirect ('add_usuarios.html')   


