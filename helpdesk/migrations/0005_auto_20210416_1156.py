# Generated by Django 3.0.11 on 2021-04-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_auto_20210416_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('aguardando', 'aguardando'), ('em atendimento', 'em atendimento'), ('fechado', 'fechado'), ('aberto', 'aberto')], default='aberto', max_length=100, verbose_name='status'),
        ),
    ]
