# Generated by Django 3.0.11 on 2021-07-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210702_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariopessoal',
            name='genero',
            field=models.CharField(blank=True, choices=[('Outro', 'Outro'), ('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='---', max_length=20, null=True, verbose_name='Genero'),
        ),
    ]
