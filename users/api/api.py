from os import execlpe
from ..models import   Area, Department, Group_permissions, Notes
from ..models import   UsuarioCorporativo, UsuarioEndereco, UsuarioTrabalho,UsuarioDocumentos, Companies, UsuarioPessoal,Office,Contabancaria
from files.models import  Dashbaners
from datetime import date, datetime
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import xlwt
import xlrd3 as xlrd
from  .serializers import Companies,Noteserializer, Officeserializer,PernonalUserserializer,CorporateUserserializer,Dashbanerserializer,Userserializer
from rest_framework.views import APIView, Response
from rest_framework import request, viewsets,views
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import MultiPartParser
from django.utils.dateparse import parse_datetime

# from .form import formRegistrationAddress,formRegistrationCorporate,formRegistrationDocuments,formRegistrationPersonal,formRegistrationWork,formRegistrationBank

class users_view(viewsets.ModelViewSet):
    serializer_class=Userserializer
    queryset = User.objects.all()


############ new view ############



class general_Banner_view(viewsets.ModelViewSet):
    serializer_class= Dashbanerserializer
    def get_queryset(self):
        objects = Dashbaners.objects.filter(geral=True).order_by("order_by")
        for object in objects:
            if object.timeshow:
                if object.timeshow < datetime.date(datetime.today()):
                    object.active  =  False
                    object.expired =True
                    object.save()
                else:
                   object.active  =  True
                   object.expired = False
                   object.save()
        query=  Dashbaners.objects.filter(paused=False,active=True,geral=True).order_by("order_by")          
        return query

class manager_Banner_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class=Dashbanerserializer  
    def get_queryset(self):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        list =[user.user,user.work.manager]
        objects = Dashbaners.objects.filter(manager__in=list).order_by("order_by")
        for object in objects:
            if object.timeshow:
                if object.timeshow < datetime.date(datetime.today()):
                    object.active  =  False
                    object.expired =True
                    object.save()
                else:
                   object.active  =  True
                   object.expired = False
                   object.save()    
        query =  Dashbaners.objects.filter(paused=False,active=True,manager__in=list).order_by("order_by")           
        return query

class all_general_Banner_view(viewsets.ModelViewSet):
    serializer_class = Dashbanerserializer
    def get_queryset(self):
        objects = Dashbaners.objects.filter(geral=True).order_by("order_by")
        for object in objects:
            if object.timeshow:
                if object.timeshow < datetime.date(datetime.today()):
                    object.active  =  False
                    object.expired =True
                    object.save()
                else:
                   object.expired = False
                   object.active  =  True
                   object.save()    
        query = Dashbaners.objects.filter(geral=True).order_by("order_by")  
        return query

class all_manager_Banner_view(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class=Dashbanerserializer  
    def get_queryset(self):
        user = UsuarioCorporativo.objects.get(user=self.request.user)
        objects = Dashbaners.objects.filter(manager=user.user).order_by("order_by")
        for object in objects:
            if object.timeshow:
                if object.timeshow < datetime.date(datetime.today()):
                    object.active  =  False
                    object.expired =True
                    object.save()
                else:
                   object.active  =  True
                   object.expired = False
                   object.save()  
        query = Dashbaners.objects.filter(manager=user.user).order_by("order_by")           
        return query
        

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
    serializer_class= Officeserializer
    queryset = Office.objects.all()

class user_birth(viewsets.ModelViewSet):
    serializer_class = PernonalUserserializer

    def get_queryset(self,format=None):
        data_atual = datetime.today()
        query = UsuarioPessoal.objects.filter(active= True,birthdate__month= str(data_atual.month)).order_by('birthdate__day')
        return query

class user_view(viewsets.ModelViewSet):
    serializer_class = CorporateUserserializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self,format=None):
        user = UsuarioCorporativo.objects.get(user= self.request.user)
        print(user.group_permission)
        if user.group_permission ==  Group_permissions.objects.get(name="Arena-Genios"):
            companies = ["ARENA VIDROS","Genios Shop"]
            query = UsuarioCorporativo.objects.filter(work__company__company_name__in=companies,active=True).order_by('code__name')
            return query
        elif user.group_permission == Group_permissions.objects.get(name="Geral"):
            query = UsuarioCorporativo.objects.filter(active=True).order_by('code__name')
            return query
        elif user.group_permission == Group_permissions.objects.get(name="Borrachauto"):
            query = UsuarioCorporativo.objects.filter(work__company__company_name="Borrachauto",active=True).order_by('code__name')
            return query
        elif user.group_permission ==  Group_permissions.objects.get(name="lotus"):
            query = UsuarioCorporativo.objects.filter(work__company__company_name="Lotus Participações",active=True).order_by('code__name')
            return query
      
        



####### APIViEW ########
class export_view(views.APIView):
        MDATA = datetime.now().strftime('%d-%m-%Y')
        def export(self,model, filename_final, queryset, columns):
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="%s"' % filename_final

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

        def put(self,request,format=None):
            MDATA = datetime.now().strftime('%Y-%m-%d')
            model = 'Users'
            filename = 'colaboradores_exportados.xls'
            _filename = filename.split('.')
            filename_final = f'{_filename[0]}_{MDATA}.{_filename[1]}'
            queryset = UsuarioCorporativo.objects.filter(active=True).order_by("code__name").values_list(
                'code__name',   
                'work__office__office',
                'work__department__department_name',
                'work__company__company_name',
                'work__admission_date',
                'code__birthdate',
            )
            columns = ('Nome', 'Cargo','Departamento','Empresa','Admissão','Data Nascimento')
          
            response = self.export(model, filename_final, queryset,columns)
            # Serializer = CorporateUserserializer(response, many=True) 
            
            return response
            
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

class user_notes_view(views.APIView):
    def get_object(self, code):
        try:
            user = UsuarioPessoal.objects.get(code=code)
            return Notes.objects.filter(code=user).order_by("-create")
        except:
            raise Http404

    def get(self, request, code, format=None):
        snippet = self.get_object(code)
        serializer = Noteserializer(snippet, many=True)
        return Response(serializer.data)

class create_user_view(views.APIView):
    permission_classes = (IsAuthenticated,)  
    parser_classes = (MultiPartParser,) 
    def post(self, request, *args, **kwargs):
        if UsuarioPessoal.objects.all():
                    Usuario_id = UsuarioPessoal.objects.all().order_by('-id')[0].code

                    codigo = Usuario_id + 1
        else:
                            codigo = 10001
        grupo =request.POST["group"]
        gs = Group.objects.get(name=grupo)  
        birthdate=  datetime.strptime(request.POST["birthdate"],"%d/%m/%Y")
        try:
            profile = request.FILES['profile_image']
        except:
            profile= None
        if not User.objects.filter(username=request.POST["user"]).exists():                      
            user = User.objects.create(username=request.POST["user"],first_name=request.POST["user"])
            user.set_password(request.POST["password"])
            user.is_active = True
            user.save()
            users = User.objects.get(username=request.POST["user"])
            UsuarioPessoal.objects.create(code=codigo,name=request.POST["name"],cpf=request.POST["cpf"],birthdate=birthdate,profile_image=profile,personal_cell=request.POST['personal_cell'])           
            u = UsuarioPessoal.objects.get(name=request.POST["name"])
            try:
                office = Office.objects.get(office=request.POST["office"])
            except:
                office=None
            try:
                company = Companies.objects.get(company_name = request.POST['company'] )
            except:
                 company=None
            try:   
                 department = Department.objects.get(department_name = request.POST['department'])
            except:
                department=None
            try:     
                area = Area.objects.get(area=request.POST['area'])
            except:
               area =None 
            try:
                admission = datetime.strptime(request.POST['admission_date'],"%d/%m/%Y")
            except:
                  admission = None      
            usua= UsuarioTrabalho.objects.create(code=u ,manager= request.POST["manager"],office=office,admission_date=admission,company=company,department=department,area=area)
            
            d = UsuarioDocumentos.objects.create(code=u)
            e = UsuarioEndereco.objects.create(code=u)
            c = Contabancaria.objects.create(code=u)
            UsuarioCorporativo.objects.create(code=u,work=usua,user=users,group=gs,document=d,address=e,bank=c)
            code = [u.code, str(u.profile_image), u.name] 
            return Response(code)
        else:
            return Response('já tem seu puto')
    def put(self,request,format=None):
        data_type = request.POST['data_type']
        code = request.POST['code']
        if data_type == "dados pessoais":
                object= UsuarioPessoal.objects.get(code=code)
                object.pis = request.POST['pis']
                object.surname = request.POST['surname']
                object.voter_title = request.POST['voter_title']
                object.work_card = request.POST['work_card']
                object.series = request.POST['series']
                object.work_card_uf = request.POST['work_card_uf']
                try:
                    object.work_card_date =datetime.strptime(request.POST['work_card_date'],"%d/%m/%Y")
                except:
                    object.work_card_date = None
                object.gender = request.POST['gender']
                object.color = request.POST['color']
                object.marital_status =request.POST['marital_status']
                object.schooling =request.POST['schooling']
                object.birthdate_uf = request.POST['birthdate_uf']
                object.city_birth =request.POST['city_birth']
                object.country_birth =request.POST['country_birth']
                object.national_country =request.POST['national_country']
                object.mother =request.POST['mother']
                object.father = request.POST['father']
                
                object.save()
                if not UsuarioDocumentos.objects.filter(code=object).exists():
                    UsuarioDocumentos.objects.create(code=object,document=request.POST['document'],document_number = request.POST['document_number'],organ= request.POST["organ"],dispatch_date =  datetime.strptime(request.POST['dispatch_date'],"%d/%m/%Y"),shelf_life =datetime.strptime(request.POST['shelf_life'],"%d/%m/%Y"))
                else :
                    second_object = UsuarioDocumentos.objects.get(code=object)
                    second_object.document =request.POST['document']
                    second_object.document_number = request.POST['document_number']
                    second_object.organ= request.POST["organ"]
                    try:
                        second_object.dispatch_date =  datetime.strptime(request.POST['dispatch_date'],"%d/%m/%Y")
                        
                    except:
                        second_object.dispatch_date =  None
                    try:
                        second_object.shelf_life = datetime.strptime(request.POST['shelf_life'],"%d/%m/%Y")
                    except:
                        second_object.shelf_life = None
                    second_object.save()
                if not UsuarioEndereco.objects.filter(code=object).exists():  
                      UsuarioEndereco.objects.create(code=object,zip_code=request.POST['zip_code'],type = request.POST['type'],public_place= request.POST["public_place"],number = request.POST['number'],uf = request.POST['uf'],city=request.POST['city'],district=request.POST['district'],complement=request.POST['complement'],country=request.POST['country'])
                else: 

                    third_object = UsuarioEndereco.objects.get(code=object)
                    third_object.zip_code=request.POST['zip_code']
                    third_object.type = request.POST['type']
                    third_object.public_place= request.POST["public_place"]
                    third_object.number = request.POST['number']
                    third_object.uf = request.POST['uf']
                    third_object.city=request.POST['city']
                    third_object.district=request.POST['district']
                    third_object.complement=request.POST['complement']
                    third_object.country=request.POST['country']
                    third_object.save()
         
                    
                return Response(status=status.HTTP_202_ACCEPTED)
        elif  data_type == "dados trabalhistas":
                user = UsuarioPessoal.objects.get(code=code)
                if  UsuarioTrabalho.objects.filter(code=user).exists():
                       object = UsuarioTrabalho.objects.get(code=user)
                       object.trnasport_voucher = request.POST['trnasport_voucher']
                     
                       
                       object.admission_type = request.POST['admission_type']
                       object.admission_indicative = request.POST['admission_indicative']
                       object.first_job = request.POST['first_job']
                       object.work_regime = request.POST['work_regime']
                       object.day_regime = request.POST['day_regime']
                       object.nature_activity = request.POST['nature_activity']
                       object.pension_scheme = request.POST['pension_scheme']
                       object.category = request.POST['category']
                       object.function_code = request.POST['function_code']
                       object.workload = request.POST['workload']
                       object.wage_unit = request.POST['wage_unit']
                       try:
                            object.variable_salary = request.POST['variable_salary']
                       except:
                           print("é essa mesmo a sujeita")     

                       try:
                            object.resignation_date =  datetime.strptime(request.POST['resignation_date'],"%d/%m/%Y")
                            third_object =  UsuarioCorporativo.objects.get(code=user)
                            user.active = False
                            user.save()
                            third_object.user=None
                            third_object.group = None
                            third_object.active = False
                            third_object.save()
                            
                       
                            
                       except:
                           object.resignation_date = None     
                       object.save()
                       try:
                            note=request.POST["note"]
                       except:
                           note= None     
                       if not note == None:
                            Notes.objects.create(code=user,note=note,creator=self.request.user)
                    #    
                                               
                else:
                  
                    object = UsuarioTrabalho.objects.create(code=user,trnasport_voucher = request.POST['trnasport_voucher'],note = request.POST['note'],admission_date = request.POST['admission_date'],admission_type = request.POST['admission_type'],admission_indicative = request.POST['admission_indicative'],first_job = request.POST['first_job'],work_regime = request.POST['work_regime'],day_regime = request.POST['day_regime'],nature_activity = request.POST['nature_activity'],category = request.POST['category'],function_code = request.POST['function_code'],workload = request.POST['workload'],wage_unit = request.POST['wage_unit'],variable_salary = request.POST['variable_salary'])

                if  Contabancaria.objects.filter(code=user).exists():
                        second_object = Contabancaria.objects.get(code=user)
                        second_object.bank=request.POST['bank']
                        second_object.agency=request.POST['agency']
                        second_object.account=request.POST['account']
                        second_object.save()
                else:
                    Contabancaria.objects.create(code=user,bank=request.POST['bank'],agency=request.POST['agency'],account=request.POST['account'])        
                return Response(status=status.HTTP_202_ACCEPTED)
        elif  data_type == "dados basicos":
            try:
                office = Office.objects.get(office=request.POST["office"])
            except:
                office = None    
            try:    
                company = Companies.objects.get(company_name = request.POST['company'] )
            except:
                company = None    
            try:    
                department = Department.objects.get(department_name = request.POST['department'])
            except:
                department =None    
            try:    
                area = Area.objects.get(area=request.POST['area'])
            except:
                area = None    
            object= UsuarioPessoal.objects.get(code=code)
            object.name=request.POST["name"]
            object.cpf=request.POST["cpf"]    
            object.birthdate= datetime.strptime(request.POST["birthdate"],"%d/%m/%Y")
            try:
                object.profile_image = request.FILES['profile_image']
            except:
                pass    
            object.personal_cell =request.POST['personal_cell']
            object.save()

            second_object = UsuarioTrabalho.objects.get(code=object)
            second_object.office = office
            second_object.admission_date = datetime.strptime(request.POST['admission_date'],"%d/%m/%Y")
            second_object.company=company
            second_object.department =department
            second_object.area =area
            second_object.manager= request.POST["manager"]
            second_object.save()
            work = UsuarioTrabalho.objects.get(code=object)
            document = UsuarioDocumentos.objects.get(code=object)
            address = UsuarioEndereco.objects.get(code=object)
            bank = Contabancaria.objects.get(code=object)
            grupo =request.POST["group"]
            gs = Group.objects.get(name=grupo)  
            third_object =  UsuarioCorporativo.objects.get(code=object)
            third_object.group = gs
            third_object.work= work
            third_object.address =address
            third_object.document =document 
            third_object.bank = bank
            third_object.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        elif data_type == "note":
            object= UsuarioPessoal.objects.get(code=code)
            Notes.objects.create(code=object,note=request.POST["note"],creator=self.request.user)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
                user = UsuarioPessoal.objects.get(code=code)
                work = UsuarioTrabalho.objects.get(code=user)
                try:
                    document = UsuarioDocumentos.objects.get(code=user)
                    address = UsuarioEndereco.objects.get(code=user)
                    bank = Contabancaria.objects.get(code=user)
                except:
                    document= None    
                    address= None    
                    bank= None    
                object =  UsuarioCorporativo.objects.get(code=user)
                object.email = request.POST['email']
                object.corporate_email = request.POST['corporate_email']
                object.skype = request.POST['skype']
                object.telephone = request.POST['telephone']
                object.corporate_phone = request.POST['corporate_phone']
                object.ramal = request.POST['ramal']
             
                object.save()
                return Response(status=status.HTTP_202_ACCEPTED)

class create_banner_view(views.APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self,request,format=None):
        image = request.FILES["bannerimage"]
        description = request.POST["description"]
        order = request.POST["order"]
        general = request.POST["general"]
        try: 
            link = request.POST['link']
        except:
            link = None    
        try:
            time = datetime.strptime(request.POST["time"],"%d/%m/%Y")
        except:
            time= None
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
                Dashbaners.objects.create(image=image,link=link,desc=description,manager=gestor,geral=general,order_by = order,timeshow=time)    
            else:
                Dashbaners.objects.create(image=image,desc=description,link=link,manager=gestor,geral=general,order_by = order,timeshow=time)
        else:
            if Dashbaners.objects.filter(order_by=order,manager=gestor).exists():
                bans= Dashbaners.objects.filter(manager=gestor,order_by__gte = order).order_by('order_by')
                for ban in bans:
                    ban.order_by = ban.order_by + 1
                    ban.save()
                Dashbaners.objects.create(image=image,desc=description,link=link,manager=gestor,geral=general,order_by = order,timeshow=time)        
            else:
                Dashbaners.objects.create(image=image,desc=description,link=link,manager=gestor,geral=general,order_by = order,timeshow=time)

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

class create_office_view(views.APIView):
    def post(self,request,format=None):
        if Office.objects.filter(office=request.POST['office']).exists():
            raise  Http404
        else:
            Office.objects.create(office=request.POST['office'],ncbo=request.POST['ncbo'])
            return Response(status=status.HTTP_201_CREATED)
