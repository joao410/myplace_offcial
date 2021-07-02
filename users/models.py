from os import name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.deletion import DO_NOTHING

from django.db.models.fields.related import ForeignKey


# Create your models here.

class Base(models.Model):
    create = models.DateField('Criacao', auto_now_add=True)
    update = models.DateField('Atualizacao', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Empresa(Base):
    cnpj  = models.CharField("cnpj",max_length=200)
    nempresa = models.CharField("NEmpresa", max_length=100,default="...")
    telefone = models.CharField("telefone",max_length=15,default="...")
   

    class Meta:
      verbose_name = "Empresa"
      verbose_name_plural = "Empresas"

    def __str__(self):
        return f'{self.nempresa} - {self.telefone}'   
class Departamento(Base):
    name = models.CharField("name",max_length=250)
    empresa = ForeignKey(Empresa,on_delete=DO_NOTHING)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.name} - {self.empresa}'   

class Cargo(Base):
    cargo  = models.CharField("cargo", max_length=100,default="...")
    descricao = models.CharField("descricao", max_length=255,default="...")
    ncbo = models.CharField("ncbo", max_length= 10,default="...")
    
    
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return f'{self.cargo} - {self.ncbo}'   





class UsuarioPessoal(Base):
    codigo = models.IntegerField("Codigo",null=True, default=None)
    nome = models.CharField("Name", max_length=250,blank=True,null=True,default="---")
    apelido = models.CharField("Apelido", max_length=100, blank=True,null=True,default="---")
    cpf = models.CharField("Cpf", max_length=20,blank=True,null=True,default="---")
    pis = models.CharField("Pis",max_length=20,blank=True,null=True,default="---")
    tituloeleitor = models.CharField("TituloEleitor",max_length=20,blank=True,null=True,default="---")
    carteiratrabalho = models.CharField("CarteiraTrabalho",max_length=20,blank=True,null=True,default="---")
    serie = models.CharField("Serie",max_length=20,blank=True,null=True,default="---")
    ufcarteiratrabalho = models.CharField("UfCarteiraTrabalho",blank=True,null=True,max_length=2,default="--")
    datacarteiratrabalho = models.DateField(blank=True,null=True)
    GENERO_CHOICES = {
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),

    }
    genero = models.CharField("Genero",max_length=20,choices=GENERO_CHOICES,blank=True,null=True, default="---")
    cor= models.CharField("Cor", max_length=20,blank=True,null=True,default="---")
    ecivil = models.CharField("Ecivil", blank=True,null=True,max_length=20,default="---")
    celpessoal = models.CharField("celpessoal", blank=True,null=True,max_length=13,default="---")
    escolaridade = models.CharField("Escolaridade", blank=True,null=True,max_length=100,default="---")
    datanacimento = models.DateField(blank=True,null=True)
    ufnacimento = models.CharField("UfNacimento",blank=True,null=True, max_length=2,default="--")
    municipionacimento = models.CharField("MunicipioNacimento", blank=True,null=True,max_length=250,default="---")
    paisnacimento = models.CharField("PaisNacimento",blank=True,null=True, max_length=100,default="---")
    paisnacionalidade = models.CharField("PaisNacionalidade",max_length=100,blank=True,null=True,default="---")
    nomemae = models.CharField("NomeMae", blank=True,null=True,max_length=100,default="---")
    nomepai= models.CharField("NomePai", blank=True,null=True,max_length=100,default="---")

    

    class Meta:
       verbose_name = "UsuarioPessoal"
       verbose_name_plural = "UsuariosPessoal"

    def __str__(self):
        return f'{self.nome} - {self.cpf}'   

class Contabancaria(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True )
    banco = models.CharField("Banco", max_length=255,blank=True,null=True,default=None)
    agencia = models.CharField("Agência", max_length=255,blank=True,null=True,default=None)
    conta = models.CharField("Conta", max_length=255,blank=True,null=True,default=None)
    class Meta:
       verbose_name = "Contabancaria"
       verbose_name_plural = "Contasbancarias"

    def __str__(self):
        return f'{self.banco} - {self.agencia} - {self.conta}'  

class UsuarioTrabalho(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True )
    empresa= models.CharField("Empresa", max_length=100,blank=True,null=True,default=None)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE, null=True, blank=True )
    departamento = models.CharField("Departamento",blank=True,null=True,max_length=100,default=None)
    valetransporte =  models.CharField("valetransporte",max_length=3,blank=True,null=True,default=None)
    obs =  models.TextField("Observação",max_length=255,blank=True,null=True,default=None)
    dataadmissao = models.DateField(blank=True,null=True)
    datademissao = models.DateField(blank=True,null=True)
    tipoAdmissao  = models.CharField("tipoAdmissao",max_length=100,blank=True,null=True,default=None)
    indicativoadmissao = models.CharField("IndicativoAdmissao",max_length=50,blank=True,null=True,default=None)
    primeiroemprego = models.CharField("PrimeiroEmprego", max_length=3,blank=True,null=True,default=None)
    regimetrabalho = models.CharField("RegimeTrabalho", max_length=10,blank=True,null=True, default=None)
    regimeprevidenciario = models.CharField("RegimePrevidenciario",blank=True,null=True,max_length=10,default=None)
    regimejornada = models.CharField("RegimeJornada", max_length=100,blank=True,null=True ,default=None)
    naturezaatividade = models.CharField("NaturezaAtividade", max_length=50 ,blank=True,null=True,default=None)
    categoria = models.CharField("Categoria",max_length=100,blank=True,null=True,default=None)
    codigofuncao = models.CharField("CodigoFuncao",max_length=20,blank=True,null=True ,default="")
    cargahorariam = models.CharField("CargaHorariaM",max_length=20,blank=True,null=True,default=None)
    unidadesalarial = models.CharField("UnidadeSalarial",max_length=15,blank=True,null=True,default=None)
    salariovariavel =  models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True,default=00.00)

    class Meta: 
       verbose_name = "UsuarioTrabalho"
       verbose_name_plural = "UsuariosTrabalho"

    def __str__(self):
        return f'{self.codigo} - {self.cargo}'   

class UsuarioDocumentos(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True )
    documento = models.CharField("Documento",max_length=5,blank=True,null=True,default=None)
    numerodocumento = models.CharField("NumeroDocumento",max_length=15,blank=True,null=True,default=None)
    orgao = models.CharField("orgao",max_length=5,blank=True,null=True,default=None)
    dataexpedissao = models.DateField(blank=True,null=True)
    validade = models.DateField(blank=True,null=True)
    class Meta:
       verbose_name = "UsuarioDocumento"
       verbose_name_plural = "UsuariosDocumentos"

    def __str__(self):
        return f'{self.documento} - {self.numerodocumento}'  


class UsuarioEndereco(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField("Cep",max_length=9,blank=True,null=True,default=None)
    tipo = models.CharField("Tipo",max_length=100,blank=True,null=True,default=None)
    logradouro = models.CharField("Logradouro",blank=True,null=True ,max_length=250,default=None)
    numero = models.CharField("Numero",max_length=5,blank=True,null=True,default=None)
    ufatual = models.CharField("UfAtual",blank=True,null=True,max_length=2,default=None)
    municipioatul = models.CharField("MunicipioAtul",max_length=50,blank=True,null=True,default=None)
    bairroatual = models.CharField("BairroAtual",max_length=50,blank=True,null=True,default=None)
    complemento = models.CharField("Complemento",max_length=20,blank=True,null=True,default=None)
    pais = models.CharField("Pais",max_length=50,blank=True,null=True,default=None)
    class Meta:
       verbose_name = "UsuarioEndereco"
       verbose_name_plural = "UsuariosEndereco"

    def __str__(self):
        return f'{self.cep} - {self.numero}'  




class UsuarioCorporativo(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True)
    trabalho = models.ForeignKey(UsuarioTrabalho,on_delete=models.CASCADE, null=True, blank=True)
    endereco = models.ForeignKey(UsuarioEndereco,on_delete=models.CASCADE, null=True, blank=True)
    documento = models.ForeignKey(UsuarioDocumentos,on_delete=models.CASCADE, null=True, blank=True)
    banco = models.ForeignKey(Contabancaria,on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.CharField("email", blank=True,null=True,max_length=100, default=None)
    emailCorporativo = models.CharField("email_corporativo", max_length=100,blank=True,null=True,default=None)
    skype = models.CharField("skype",max_length=100,blank=True,null=True,default=None) 
    telefone = models.CharField("telefone", max_length=13,blank=True,null=True,default=None)
    tel = models.CharField("tel", max_length=13,blank=True,null=True, default=None)
    ramal = models.CharField("ramal", max_length=4,blank=True,null=True, default=None)
    usuario = models.ForeignKey(User,on_delete=models.DO_NOTHING )
    grupo = models.ForeignKey(Group,on_delete=models.DO_NOTHING)    

    class Meta:
       verbose_name = "UsuarioCorporativo"
       verbose_name_plural = "UsuariosCorporativo"

    def __str__(self):
        return f'{self.email} - {self.telefone}'   

def get_files_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'chamado/images/{uuid.uuid4()}.{ext}'
    return filename
class ImagePerfil(Base):
    nome = models.CharField("nome", max_length=100,blank=True,null=True,default=None)
    image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    obs = models.TextField(null=True, blank=True, default=None)
   
   
   
    class Meta:
       verbose_name = "ImagePerfil"
       verbose_name_plural = "ImagensPerfil"


    def __str__(self):
        return f'{self.id} - {self.nome}'    








