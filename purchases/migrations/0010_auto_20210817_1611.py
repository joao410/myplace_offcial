# Generated by Django 3.0.11 on 2021-08-17 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0009_purchase_requisition_return_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition_product',
            name='purchase_requisition_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='purchases.Purchase_requisition'),
        ),
    ]
