from django.contrib import admin
from users.models import UsuarioPessoal,UsuarioTrabalho,UsuarioDocumentos,UsuarioEndereco,UsuarioCorporativo, ImagePerfil,Empresa,Cargo,Contabancaria


# Register your models here.


@admin.register(UsuarioPessoal)
class UsuarioPessoalAdmin(admin.ModelAdmin):
    list_display = ('create','active','codigo','nome','apelido','cpf','pis','tituloeleitor','carteiratrabalho','serie','ufcarteiratrabalho','datacarteiratrabalho','genero','cor','ecivil','escolaridade','datanacimento', 'ufnacimento','municipionacimento','paisnacimento','paisnacionalidade','nomemae','nomepai',)
    search_fields = ('create','active','codigo','nome','apelido','cpf','pis','tituloeleitor','carteiratrabalho','serie','ufcarteiratrabalho','datacarteiratrabalho','genero','cor','ecivil','escolaridade','datanacimento', 'ufnacimento','municipionacimento','paisnacimento','paisnacionalidade','nomemae','nomepai',)
@admin.register(UsuarioCorporativo)
class UsuarioCorporativoAdmin(admin.ModelAdmin):
    list_display = ('create','active','id','codigo','email','emailCorporativo','skype','telefone','tel','ramal','usuario', 'grupo',)
    search_fields = ('create','active','id','codigo','email','emailCorporativo','skype','telefone','tel','ramal','usuario', 'grupo',)
@admin.register(UsuarioTrabalho)
class UsuarioTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('create','active','codigo','cargo','tipoAdmissao','departamento','empresa', 'valetransporte','dataadmissao','datademissao','indicativoadmissao','primeiroemprego','regimetrabalho','regimeprevidenciario','regimejornada','naturezaatividade','categoria','codigofuncao','cargahorariam','unidadesalarial','salariovariavel',)
    search_fields = ('create','active','codigo','cargo','tipoAdmissao','departamento','empresa', 'valetransporte','dataadmissao','datademissao','indicativoadmissao','primeiroemprego','regimetrabalho','regimeprevidenciario','regimejornada','naturezaatividade','categoria','codigofuncao','cargahorariam','unidadesalarial','salariovariavel',)
@admin.register(UsuarioDocumentos)
class UsuarioDocumentosAdmin(admin.ModelAdmin):
    list_display = ('create','active','codigo','documento','numerodocumento','orgao','dataexpedissao','validade',)
    search_fields = ('create','active','codigo','documento','numerodocumento','orgao','dataexpedissao','validade',)

@admin.register(UsuarioEndereco)
class UsuarioEnderecoAdmin(admin.ModelAdmin):
    list_display = ('create','active','codigo','cep','tipo','logradouro','numero','ufatual','municipioatul','bairroatual','complemento','pais')
    search_fields =('create','active','codigo','cep','tipo','logradouro','numero','ufatual','municipioatul','bairroatual','complemento','pais')


@admin.register(ImagePerfil)
class ImagePerfilAdmin(admin.ModelAdmin):
    list_display = ('create','active','nome','obs', 'image',)
    search_fields =('create','active','nome','obs', 'image',)



@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','nempresa','telefone', 'cnpj',)
    search_fields =('id','create','active','nempresa','telefone', 'cnpj',)
@admin.register(Cargo)
class cargoAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','cargo','descricao', 'ncbo',)
    search_fields = ('id','create','active','cargo','descricao', 'ncbo',)
@admin.register(Contabancaria)
class contabancariaAdmin(admin.ModelAdmin):
    list_display = ('id','create','active','codigo','banco','agencia', 'conta',)
    search_fields = ('id','create','active','codigo','banco','agencia', 'conta',)

   
