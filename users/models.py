from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid


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
    codigo = models.IntegerField("Codigo",default="0")
    nome = models.CharField("Name", max_length=250, default="#")
    apelido = models.CharField("Apelido", max_length=100, default="#")
    cpf = models.CharField("Cpf", max_length=20, default="0")
    pis = models.IntegerField("Pis",default="0")
    tituloeleitor = models.IntegerField("TituloEleitor",default=".0")
    carteiratrabalho = models.IntegerField("CarteiraTrabalho",default="0")
    serie = models.IntegerField("Serie",default="0")
    ufcarteiratrabalho = models.CharField("UfCarteiraTrabalho",max_length=2,default="..")
    datacarteiratrabalho = models.DateField(blank=True,null=True)
    GENERO_CHOICES = {
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),

    }
    genero = models.CharField("Genero",max_length=20,choices=GENERO_CHOICES, default="#")
    cor= models.CharField("Cor", max_length=20, default="#")
    ecivil = models.CharField("Ecivil", max_length=20,default="#")
    celpessoal = models.CharField("celpessoal", max_length=13,default="...")
    escolaridade = models.CharField("Escolaridade", max_length=100, default="#")
    datanacimento = models.DateField(blank=True,null=True)
    ufnacimento = models.CharField("UfNacimento", max_length=2,default="#")
    municipionacimento = models.CharField("MunicipioNacimento", max_length=250,default="#")
    paisnacimento = models.CharField("PaisNacimento", max_length=100,default="#")
    paisnacionalidade = models.CharField("PaisNacionalidade",max_length=100,default="#")
    nomemae = models.CharField("NomeMae", max_length=100,default="não consta")
    nomepai= models.CharField("NomePai", max_length=100,default="não consta")

    

    class Meta:
       verbose_name = "UsuarioPessoal"
       verbose_name_plural = "UsuariosPessoal"

    def __str__(self):
        return f'{self.nome} - {self.cpf}'   



class UsuarioTrabalho(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True )
    empresa= models.CharField("Empresa", max_length=100,default="#")
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE, null=True, blank=True )
    departamento = models.CharField("Departamento",max_length=100,default="...")
    valetransporte =  models.CharField("valetransporte",max_length=3,default="...")
    dataadmissao = models.DateField(blank=True,null=True)
    datademissao = models.DateField(blank=True,null=True)
    tipoAdmissao  = models.CharField("tipoAdmissao",max_length=100,default="...")
    indicativoadmissao = models.CharField("IndicativoAdmissao",max_length=50,default="...")
    primeiroemprego = models.CharField("PrimeiroEmprego", max_length=3,default="...")
    regimetrabalho = models.CharField("RegimeTrabalho", max_length=10, default="...")
    regimeprevidenciario = models.CharField("RegimePrevidenciario",max_length=10, default="...")
    regimejornada = models.CharField("RegimeJornada", max_length=100, default="...")
    naturezaatividade = models.CharField("NaturezaAtividade", max_length=50 ,default="..")
    categoria = models.CharField("Categoria",max_length=100, default="...")
    codigofuncao = models.IntegerField("CodigoFuncao", default="1")
    cargahorariam = models.CharField("CargaHorariaM",max_length=20,default="...")
    unidadesalarial = models.CharField("UnidadeSalarial",max_length=15, default="..")
    salariovariavel =  models.DecimalField(max_digits=6, decimal_places=2,default="0")

    class Meta: 
       verbose_name = "UsuarioTrabalho"
       verbose_name_plural = "UsuariosTrabalho"

    def __str__(self):
        return f'{self.codigo} - {self.cargo}'   

class UsuarioDocumentos(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True )
    documento = models.CharField("Documento",max_length=5,default="..")
    numerodocumento = models.IntegerField("NumeroDocumento",default="..")
    orgao = models.CharField("orgao",max_length=5,default="...")
    dataexpedissao = models.DateField(blank=True,null=True)
    validade = models.DateField(blank=True,null=True)
    class Meta:
       verbose_name = "UsuarioDocumento"
       verbose_name_plural = "UsuariosDocumentos"

    def __str__(self):
        return f'{self.documento} - {self.numerodocumento}'  


class UsuarioEndereco(Base):
    codigo = models.ForeignKey(UsuarioPessoal,on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField("Cep",max_length=9,default="...")
    tipo = models.CharField("Tipo",max_length=2,default="...")
    logradouro = models.CharField("Logradouro", max_length=250,default="...")
    numero = models.IntegerField("Numero",default="0")
    ufatual = models.CharField("UfAtual",max_length=2,default="...")
    municipioatul = models.CharField("MunicipioAtul",max_length=50,default="...")
    bairroatual = models.CharField("BairroAtual",max_length=50,default="...")
    complemento = models.CharField("Complemento",max_length=20,default="...")
    pais = models.CharField("Pais",max_length=50,default="....")
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
    email = models.CharField("email", max_length=100, default="#")
    emailCorporativo = models.CharField("email_corporativo", max_length=100,default="#")
    skype = models.CharField("skype",max_length=100,default="---") 
    telefone = models.CharField("telefone", max_length=13, default="---")
    tel = models.CharField("tel", max_length=13, default="---")
    ramal = models.CharField("ramal", max_length=4, default="---")
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
    nome = models.CharField("nome", max_length=100,default="#")
    image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    obs = models.TextField(null=True, blank=True, default='#')
   
   
   
    class Meta:
       verbose_name = "ImagePerfil"
       verbose_name_plural = "ImagensPerfil"


    def __str__(self):
        return f'{self.id} - {self.nome}'    





