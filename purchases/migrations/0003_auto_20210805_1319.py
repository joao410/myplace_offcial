# Generated by Django 3.0.11 on 2021-08-05 16:19

from django.db import migrations, models
import purchases.models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_auto_20210805_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition_product',
            name='payment_voucher',
            field=models.FileField(blank=True, null=True, upload_to=purchases.models.get_files_voucher),
        ),
    ]