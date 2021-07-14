# Generated by Django 3.0.11 on 2021-07-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20210713_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('aberto', 'aberto'), ('em atendimento', 'em atendimento'), ('aguardando', 'aguardando'), ('resolvido', 'resolvido')], default='aberto', max_length=100, verbose_name='status'),
        ),
    ]