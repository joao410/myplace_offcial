# Generated by Django 3.0.11 on 2021-04-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210413_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodocumentos',
            name='numerodocumento',
            field=models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='NumeroDocumento'),
        ),
        migrations.AlterField(
            model_name='usuarioendereco',
            name='numero',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='apelido',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='Apelido'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='carteiratrabalho',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='CarteiraTrabalho'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='celpessoal',
            field=models.CharField(blank=True, default='---', max_length=13, null=True, verbose_name='celpessoal'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='cor',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='cpf',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='Cpf'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='ecivil',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='Ecivil'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='escolaridade',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='Escolaridade'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='genero',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], default='---', max_length=20, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='municipionacimento',
            field=models.CharField(blank=True, default='---', max_length=250, null=True, verbose_name='MunicipioNacimento'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='nome',
            field=models.CharField(blank=True, default='---', max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='nomemae',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='NomeMae'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='nomepai',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='NomePai'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='paisnacimento',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='PaisNacimento'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='paisnacionalidade',
            field=models.CharField(blank=True, default='---', max_length=100, null=True, verbose_name='PaisNacionalidade'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='pis',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='Pis'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='serie',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='Serie'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='tituloeleitor',
            field=models.CharField(blank=True, default='---', max_length=20, null=True, verbose_name='TituloEleitor'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='ufcarteiratrabalho',
            field=models.CharField(blank=True, default='---', max_length=2, null=True, verbose_name='UfCarteiraTrabalho'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='ufnacimento',
            field=models.CharField(blank=True, default='--', max_length=2, null=True, verbose_name='UfNacimento'),
        ),
        migrations.AlterField(
            model_name='usuariotrabalho',
            name='codigofuncao',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='CodigoFuncao'),
        ),
    ]
