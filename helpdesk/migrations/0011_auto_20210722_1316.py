# Generated by Django 3.0.11 on 2021-07-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0010_auto_20210715_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chamado',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('resolvido', 'resolvido'), ('aberto', 'aberto'), ('em atendimento', 'em atendimento'), ('aguardando', 'aguardando')], default='aberto', max_length=100, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='urgency',
            field=models.CharField(choices=[('Baixa', 'Baixa'), ('Media', 'Media'), ('Alta', 'Alta')], default=None, max_length=10, verbose_name='urgencia'),
        ),
    ]