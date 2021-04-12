# Generated by Django 3.0.11 on 2021-04-08 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cargo', models.CharField(default='...', max_length=100, verbose_name='cargo')),
                ('descricao', models.CharField(default='...', max_length=255, verbose_name='descricao')),
                ('ncbo', models.CharField(default='...', max_length=10, verbose_name='ncbo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cnpj', models.CharField(max_length=200, verbose_name='cnpj')),
                ('nempresa', models.CharField(default='...', max_length=100, verbose_name='NEmpresa')),
                ('telefone', models.CharField(default='...', max_length=15, verbose_name='telefone')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='ImagePerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(default=None, max_length=100, verbose_name='nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.get_files_path)),
                ('obs', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'ImagePerfil',
                'verbose_name_plural': 'ImagensPerfil',
            },
        ),
        migrations.CreateModel(
            name='UsuarioPessoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('codigo', models.IntegerField(default=None, null=True, verbose_name='Codigo')),
                ('nome', models.CharField(default=None, max_length=250, verbose_name='Name')),
                ('apelido', models.CharField(default=None, max_length=100, verbose_name='Apelido')),
                ('cpf', models.CharField(default=None, max_length=20, verbose_name='Cpf')),
                ('pis', models.IntegerField(default='1', verbose_name='Pis')),
                ('tituloeleitor', models.IntegerField(default=None, verbose_name='TituloEleitor')),
                ('carteiratrabalho', models.IntegerField(default=None, verbose_name='CarteiraTrabalho')),
                ('serie', models.IntegerField(default='0', verbose_name='Serie')),
                ('ufcarteiratrabalho', models.CharField(default=None, max_length=2, verbose_name='UfCarteiraTrabalho')),
                ('datacarteiratrabalho', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], default=None, max_length=20, verbose_name='Genero')),
                ('cor', models.CharField(default=None, max_length=20, verbose_name='Cor')),
                ('ecivil', models.CharField(default=None, max_length=20, verbose_name='Ecivil')),
                ('celpessoal', models.CharField(default=None, max_length=13, verbose_name='celpessoal')),
                ('escolaridade', models.CharField(default=None, max_length=100, verbose_name='Escolaridade')),
                ('datanacimento', models.DateField(blank=True, null=True)),
                ('ufnacimento', models.CharField(default=None, max_length=2, verbose_name='UfNacimento')),
                ('municipionacimento', models.CharField(default=None, max_length=250, verbose_name='MunicipioNacimento')),
                ('paisnacimento', models.CharField(default=None, max_length=100, verbose_name='PaisNacimento')),
                ('paisnacionalidade', models.CharField(default=None, max_length=100, verbose_name='PaisNacionalidade')),
                ('nomemae', models.CharField(default=None, max_length=100, verbose_name='NomeMae')),
                ('nomepai', models.CharField(default=None, max_length=100, verbose_name='NomePai')),
            ],
            options={
                'verbose_name': 'UsuarioPessoal',
                'verbose_name_plural': 'UsuariosPessoal',
            },
        ),
        migrations.CreateModel(
            name='UsuarioTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('empresa', models.CharField(default=None, max_length=100, verbose_name='Empresa')),
                ('departamento', models.CharField(default=None, max_length=100, verbose_name='Departamento')),
                ('valetransporte', models.CharField(default=None, max_length=3, verbose_name='valetransporte')),
                ('dataadmissao', models.DateField(blank=True, null=True)),
                ('datademissao', models.DateField(blank=True, null=True)),
                ('tipoAdmissao', models.CharField(default=None, max_length=100, verbose_name='tipoAdmissao')),
                ('indicativoadmissao', models.CharField(default=None, max_length=50, verbose_name='IndicativoAdmissao')),
                ('primeiroemprego', models.CharField(default=None, max_length=3, verbose_name='PrimeiroEmprego')),
                ('regimetrabalho', models.CharField(default=None, max_length=10, verbose_name='RegimeTrabalho')),
                ('regimeprevidenciario', models.CharField(default=None, max_length=10, verbose_name='RegimePrevidenciario')),
                ('regimejornada', models.CharField(default=None, max_length=100, verbose_name='RegimeJornada')),
                ('naturezaatividade', models.CharField(default=None, max_length=50, verbose_name='NaturezaAtividade')),
                ('categoria', models.CharField(default=None, max_length=100, verbose_name='Categoria')),
                ('codigofuncao', models.IntegerField(default=None, verbose_name='CodigoFuncao')),
                ('cargahorariam', models.CharField(default=None, max_length=20, verbose_name='CargaHorariaM')),
                ('unidadesalarial', models.CharField(default=None, max_length=15, verbose_name='UnidadeSalarial')),
                ('salariovariavel', models.DecimalField(decimal_places=2, default=None, max_digits=6)),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cargo')),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioPessoal')),
            ],
            options={
                'verbose_name': 'UsuarioTrabalho',
                'verbose_name_plural': 'UsuariosTrabalho',
            },
        ),
        migrations.CreateModel(
            name='UsuarioEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cep', models.CharField(default=None, max_length=9, verbose_name='Cep')),
                ('tipo', models.CharField(default=None, max_length=2, verbose_name='Tipo')),
                ('logradouro', models.CharField(default=None, max_length=250, verbose_name='Logradouro')),
                ('numero', models.IntegerField(default=None, verbose_name='Numero')),
                ('ufatual', models.CharField(default=None, max_length=2, verbose_name='UfAtual')),
                ('municipioatul', models.CharField(default=None, max_length=50, verbose_name='MunicipioAtul')),
                ('bairroatual', models.CharField(default=None, max_length=50, verbose_name='BairroAtual')),
                ('complemento', models.CharField(default=None, max_length=20, verbose_name='Complemento')),
                ('pais', models.CharField(default=None, max_length=50, verbose_name='Pais')),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioPessoal')),
            ],
            options={
                'verbose_name': 'UsuarioEndereco',
                'verbose_name_plural': 'UsuariosEndereco',
            },
        ),
        migrations.CreateModel(
            name='UsuarioDocumentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('documento', models.CharField(default=None, max_length=5, verbose_name='Documento')),
                ('numerodocumento', models.IntegerField(default=None, verbose_name='NumeroDocumento')),
                ('orgao', models.CharField(default=None, max_length=5, verbose_name='orgao')),
                ('dataexpedissao', models.DateField(blank=True, null=True)),
                ('validade', models.DateField(blank=True, null=True)),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioPessoal')),
            ],
            options={
                'verbose_name': 'UsuarioDocumento',
                'verbose_name_plural': 'UsuariosDocumentos',
            },
        ),
        migrations.CreateModel(
            name='UsuarioCorporativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('email', models.CharField(default=None, max_length=100, verbose_name='email')),
                ('emailCorporativo', models.CharField(default=None, max_length=100, verbose_name='email_corporativo')),
                ('skype', models.CharField(default=None, max_length=100, verbose_name='skype')),
                ('telefone', models.CharField(default=None, max_length=13, verbose_name='telefone')),
                ('tel', models.CharField(default=None, max_length=13, verbose_name='tel')),
                ('ramal', models.CharField(default=None, max_length=4, verbose_name='ramal')),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioPessoal')),
                ('documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioDocumentos')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioEndereco')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Group')),
                ('trabalho', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsuarioTrabalho')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UsuarioCorporativo',
                'verbose_name_plural': 'UsuariosCorporativo',
            },
        ),
    ]
