# Generated by Django 3.0.11 on 2021-04-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210413_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariopessoal',
            name='genero',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Outro', 'Outro'), ('Feminino', 'Feminino')], default='---', max_length=20, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='usuariopessoal',
            name='ufcarteiratrabalho',
            field=models.CharField(blank=True, default='--', max_length=2, null=True, verbose_name='UfCarteiraTrabalho'),
        ),
    ]
