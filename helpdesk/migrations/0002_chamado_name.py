# Generated by Django 3.0.11 on 2021-07-01 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UsuarioPessoal'),
        ),
    ]
