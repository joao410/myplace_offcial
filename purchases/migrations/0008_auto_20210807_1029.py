# Generated by Django 3.0.11 on 2021-08-07 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0007_purchase_requisition_observation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_requisition',
            old_name='observation',
            new_name='note',
        ),
    ]
