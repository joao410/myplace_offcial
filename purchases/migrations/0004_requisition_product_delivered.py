# Generated by Django 3.0.11 on 2021-08-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_auto_20210805_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition_product',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
