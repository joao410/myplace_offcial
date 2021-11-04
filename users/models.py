from os import name

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, DateTimeField

from django.db.models.fields.related import ForeignKey
from django.db.models.manager import Manager


# Create your models here.


class Base(models.Model):
    create = models.DateField("Criacao", auto_now_add=True)
    update = models.DateField("Atualizacao", auto_now=True)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


def get_files_path(_instance, filename):
    ext = filename.split(".")[-1]
    filename = f"users/images/{uuid.uuid4()}.{ext}"
    return filename


def get_file_path(_instance, filename):
    ext = filename.split(".")[-1]
    filename = f"users/payslip/{uuid.uuid4()}.{ext}"
    return filename


class Companies(Base):
    cnpj = models.CharField("cnpj", max_length=200)
    company_name = models.CharField("NEmpresa", max_length=100, default="...")
    phone_number = models.CharField("telefone", max_length=15, default="...")
    pabx_server = models.CharField(
        "Servidor pabx", max_length=100, blank=True, null=True
    )
    pabx_proxy = models.CharField("Proxy pabx", max_length=100, blank=True, null=True)
    pabx_domain = models.CharField(
        "Dominio pabx", max_length=100, blank=True, null=True
    )
    pabx_passwod = models.CharField("Senha pabx", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f"{self.company_name} - {self.phone_number}"


class Area(Base):
    area = models.CharField("Area", max_length=100, blank=True, null=True)
    company = models.ForeignKey(Companies, on_delete=DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return f"{self.area}-{self.company} "


class Department(Base):
    department_name = models.CharField("name", max_length=250)
    area = models.ForeignKey(Area, on_delete=DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f"{self.department_name} - {self.area}"


class Office(Base):
    office = models.CharField("cargo", max_length=100, default="...")
    description = models.CharField("descricao", max_length=255, default="...")
    ncbo = models.CharField("ncbo", max_length=10, default="...")
    department = models.ForeignKey(
        Department, on_delete=DO_NOTHING, null=True, blank=True
    )

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return f"{self.office} - {self.ncbo}"


class UsuarioPessoal(Base):
    code = models.IntegerField("Codigo", null=True, default=None)
    name = models.CharField(
        "Name", max_length=250, blank=True, null=True, default="---"
    )
    surname = models.CharField(
        "Apelido", max_length=100, blank=True, null=True, default="---"
    )
    cpf = models.CharField("Cpf", max_length=20, blank=True, null=True, default="---")
    pis = models.CharField("Pis", max_length=20, blank=True, null=True, default="---")
    voter_title = models.CharField(
        "TituloEleitor", max_length=20, blank=True, null=True, default="---"
    )
    work_card = models.CharField(
        "CarteiraTrabalho", max_length=20, blank=True, null=True, default="---"
    )
    series = models.CharField(
        "Serie", max_length=20, blank=True, null=True, default="---"
    )
    work_card_uf = models.CharField(
        "UfCarteiraTrabalho", blank=True, null=True, max_length=2, default="--"
    )
    work_card_date = models.DateField(blank=True, null=True)
    GENERO_CHOICES = {
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("Outro", "Outro"),
    }
    gender = models.CharField(
        "Genero",
        max_length=20,
        choices=GENERO_CHOICES,
        blank=True,
        null=True,
        default="---",
    )
    color = models.CharField("Cor", max_length=20, blank=True, null=True, default="---")
    marital_status = models.CharField(
        "Ecivil", blank=True, null=True, max_length=20, default="---"
    )
    personal_cell = models.CharField(
        "celpessoal", blank=True, null=True, max_length=13, default="---"
    )
    schooling = models.CharField(
        "Escolaridade", blank=True, null=True, max_length=100, default="---"
    )
    birthdate = models.DateField(blank=True, null=True)
    birthdate_uf = models.CharField(
        "UfNacimento", blank=True, null=True, max_length=2, default="--"
    )
    city_birth = models.CharField(
        "MunicipioNacimento", blank=True, null=True, max_length=250, default="---"
    )
    country_birth = models.CharField(
        "PaisNacimento", blank=True, null=True, max_length=100, default="---"
    )
    national_country = models.CharField(
        "PaisNacionalidade", max_length=100, blank=True, null=True, default="---"
    )
    mother = models.CharField(
        "NomeMae", blank=True, null=True, max_length=100, default="---"
    )
    father = models.CharField(
        "NomePai", blank=True, null=True, max_length=100, default="---"
    )
    profile_image = models.ImageField(upload_to=get_files_path, null=True, blank=True)
    cod_mec = models.CharField(
        "codigo mecauto", blank=True, null=True, max_length=100, default=None
    )
    class Meta:
        verbose_name = "UsuarioPessoal"
        verbose_name_plural = "UsuariosPessoal"

    def __str__(self):
        return f"{self.name} - {self.cpf}"


class Contabancaria(Base):
    code = models.ForeignKey(
        UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True
    )
    bank = models.CharField(
        "Banco", max_length=255, blank=True, null=True, default=None
    )
    agency = models.CharField(
        "Agência", max_length=255, blank=True, null=True, default=None
    )
    account = models.CharField(
        "Conta", max_length=255, blank=True, null=True, default=None
    )

    class Meta:
        verbose_name = "Contabancaria"
        verbose_name_plural = "Contasbancarias"

    def __str__(self):
        return f"{self.bank} - {self.agency} "


class UsuarioTrabalho(Base):
    code = models.ForeignKey(
        UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True
    )
    company = models.ForeignKey(Companies, on_delete=DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=DO_NOTHING, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True
    )
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.CharField("Gestor", max_length=100, blank=True, null=True)
    trnasport_voucher = models.CharField(
        "valetransporte", max_length=3, blank=True, null=True, default=None
    )
    note = models.TextField(
        "Observação", max_length=255, blank=True, null=True, default=None
    )
    admission_date = models.DateField(blank=True, null=True)
    resignation_date = models.DateField(blank=True, null=True)
    admission_type = models.CharField(
        "tipoAdmissao", max_length=100, blank=True, null=True, default=None
    )
    admission_indicative = models.CharField(
        "IndicativoAdmissao", max_length=50, blank=True, null=True, default=None
    )
    first_job = models.CharField(
        "PrimeiroEmprego", max_length=3, blank=True, null=True, default=None
    )
    work_regime = models.CharField(
        "RegimeTrabalho", max_length=10, blank=True, null=True, default=None
    )
    pension_scheme = models.CharField(
        "RegimePrevidenciario", blank=True, null=True, max_length=10, default=None
    )
    day_regime = models.CharField(
        "RegimeJornada", max_length=100, blank=True, null=True, default=None
    )
    nature_activity = models.CharField(
        "NaturezaAtividade", max_length=50, blank=True, null=True, default=None
    )
    category = models.CharField(
        "Categoria", max_length=100, blank=True, null=True, default=None
    )
    function_code = models.CharField(
        "CodigoFuncao", max_length=20, blank=True, null=True, default=""
    )
    workload = models.CharField(
        "CargaHorariaM", max_length=20, blank=True, null=True, default=None
    )
    wage_unit = models.CharField(
        "UnidadeSalarial", max_length=15, blank=True, null=True, default=None
    )
    variable_salary = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=00.00
    )

    class Meta:
        verbose_name = "UsuarioTrabalho"
        verbose_name_plural = "UsuariosTrabalho"

    def __str__(self):
        return f"{self.code} - {self.office}"


class UsuarioDocumentos(Base):
    code = models.ForeignKey(
        UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True
    )
    document = models.CharField(
        "Documento", max_length=5, blank=True, null=True, default=None
    )
    document_number = models.CharField(
        "NumeroDocumento", max_length=15, blank=True, null=True, default=None
    )
    organ = models.CharField("orgao", max_length=5, blank=True, null=True, default=None)
    dispatch_date = models.DateField(blank=True, null=True)
    shelf_life = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "UsuarioDocumento"
        verbose_name_plural = "UsuariosDocumentos"

    def __str__(self):
        return f"{self.document} - {self.document_number}"


class UsuarioEndereco(Base):
    code = models.ForeignKey(
        UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True
    )
    zip_code = models.CharField(
        "Cep", max_length=9, blank=True, null=True, default=None
    )
    type = models.CharField("Tipo", max_length=100, blank=True, null=True, default=None)
    public_place = models.CharField(
        "Logradouro", blank=True, null=True, max_length=250, default=None
    )
    number = models.CharField(
        "Numero", max_length=5, blank=True, null=True, default=None
    )
    uf = models.CharField("UfAtual", blank=True, null=True, max_length=2, default=None)
    city = models.CharField(
        "MunicipioAtul", max_length=50, blank=True, null=True, default=None
    )
    district = models.CharField(
        "BairroAtual", max_length=50, blank=True, null=True, default=None
    )
    complement = models.CharField(
        "Complemento", max_length=20, blank=True, null=True, default=None
    )
    country = models.CharField(
        "Pais", max_length=50, blank=True, null=True, default=None
    )

    class Meta:
        verbose_name = "UsuarioEndereco"
        verbose_name_plural = "UsuariosEndereco"

    def __str__(self):
        return f"{self.zip_code} - {self.number}"

class Group_permissions(Base):
    name =  models.CharField("nome do grupo",max_length=100,blank=True,default=None)
    class Meta:
        verbose_name = "grupo de permissões"
        verbose_name_plural = "grupos de permissões"

    def __str__(self):
        return f"{self.name}"



class UsuarioCorporativo(Base):
    code = models.ForeignKey(UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True)
    work = models.ForeignKey(UsuarioTrabalho, on_delete=models.CASCADE, null=True, blank=True
    )
    address = models.ForeignKey(
        UsuarioEndereco, on_delete=models.CASCADE, null=True, blank=True
    )
    document = models.ForeignKey(
        UsuarioDocumentos, on_delete=models.CASCADE, null=True, blank=True
    )
    bank = models.ForeignKey(
        Contabancaria, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    email = models.CharField(
        "email", blank=True, null=True, max_length=100, default=None
    )
    corporate_email = models.CharField(
        "email_corporativo", max_length=100, blank=True, null=True, default=None
    )
    skype = models.CharField(
        "skype", max_length=100, blank=True, null=True, default=None
    )
    telephone = models.CharField(
        "telefone", max_length=13, blank=True, null=True, default=None
    )
    corporate_phone = models.CharField(
        "tel", max_length=13, blank=True, null=True, default=None
    )
    ramal = models.CharField("ramal", max_length=4, blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True, blank=True)
    group_permission = models.ForeignKey(Group_permissions,on_delete=DO_NOTHING,null=True,blank=True,default=None)

    class Meta:
        verbose_name = "UsuarioCorporativo"
        verbose_name_plural = "UsuariosCorporativo"

    def __str__(self):
        return f"{self.email} - {self.telephone}"


class Payslip(Base):
    code = models.ForeignKey(UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=get_file_path)
    class Meta:
        verbose_name = "holerite"
        verbose_name_plural = "hokerites"

    def __str__(self):
        return f"{self.code} - {self.file}"


class Notes(Base):
    code = models.ForeignKey(UsuarioPessoal, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField("observações", max_length=500, blank=True)
    creator = models.TextField("creator", max_length=500, blank=True, default="")

    class Meta:
        verbose_name = "observação"
        verbose_name_plural = "observações"

    def __str__(self):
        return f"{self.code} - {self.note}"

