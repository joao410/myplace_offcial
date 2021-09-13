# Generated by Django 3.0.11 on 2021-08-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20210821_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('aberto', 'aberto'), ('em atendimento', 'em atendimento'), ('resolvido', 'resolvido'), ('aguardando', 'aguardando')], default='aberto', max_length=100, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='urgency',
            field=models.CharField(choices=[('Media', 'Media'), ('Alta', 'Alta'), ('Baixa', 'Baixa')], default=None, max_length=10, verbose_name='urgencia'),
        ),
    ]