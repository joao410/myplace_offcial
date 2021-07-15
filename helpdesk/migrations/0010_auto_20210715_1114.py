# Generated by Django 3.0.11 on 2021-07-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0009_auto_20210714_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status',
            field=models.CharField(choices=[('em atendimento', 'em atendimento'), ('resolvido', 'resolvido'), ('aberto', 'aberto'), ('aguardando', 'aguardando')], default='aberto', max_length=100, verbose_name='status'),
        ),
    ]
