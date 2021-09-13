from django.contrib import admin
from users.models import  Companies, Department, Office, UsuarioPessoal,UsuarioTrabalho,UsuarioDocumentos,UsuarioEndereco,UsuarioCorporativo,Contabancaria,Area


# Register your models here.


@admin.register(UsuarioPessoal)
class UsuarioPessoalAdmin(admin.ModelAdmin):
    list_display = ('create','active','code','name','surname','cpf','pis','voter_title','work_card','series','work_card_uf','work_card_date','gender','color','marital_status','schooling','birthdate', 'birthdate_uf','city_birth','country_birth','national_country','mother','father',"profile_image",)
    search_fields = ('create','active','code','name','surname','cpf','pis','voter_title','work_card','series','work_card_uf','work_card_date','gender','color','marital_status','schooling','birthdate', 'birthdate_uf','city_birth','country_birth','national_country','mother','father',"profile_image",)
@admin.register(UsuarioCorporativo)
class UsuarioCorporativoAdmin(admin.ModelAdmin):
    list_display = ('create','active','id','code','work','corporate_email','skype','telephone','corporate_phone','ramal','user', 'group',)
    search_fields = ('create','active','id','code','work','corporate_email','skype','telephone','corporate_phone','ramal','user', 'group',)

@admin.register(UsuarioTrabalho)
class UsuarioTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('create','active','code','office','department','company', )
    search_fields =  ('create','active','code','office','department','company',)
@admin.register(UsuarioDocumentos)
class UsuarioDocumentosAdmin(admin.ModelAdmin):
    list_display = ('create','active','code','document','document_number','organ','dispatch_date','shelf_life',)
    search_fields = ('create','active','code','document','document_number','organ','dispatch_date','shelf_life',)

@admin.register(UsuarioEndereco)
class UsuarioEnderecoAdmin(admin.ModelAdmin):
    list_display = ('create','active','code','zip_code','city','country')
    search_fields = ('create','active','code','zip_code','city','country')




@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','company_name','phone_number', 'cnpj',)
    search_fields =('id','create','active','company_name','phone_number', 'cnpj',)
@admin.register(Department)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','department_name','area',)
    search_fields =('id','create','active','department_name','area',)
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','area',)
    search_fields =('id','create','active','area',)
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','office','description')
    search_fields =  ('id','create','active','office','description')
@admin.register(Contabancaria)
class contabancariaAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','code','bank','agency', 'account',)
    search_fields = ('id','create','active','code','bank','agency', 'account',)

   
