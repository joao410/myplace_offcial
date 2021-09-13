# Generated by Django 3.0.11 on 2021-08-19 13:20

from django.db import migrations, models
import purchases.models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0012_auto_20210817_1624'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_image',
        ),
        migrations.AddField(
            model_name='purchase_requisition',
            name='sector',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='setor'),
        ),
        migrations.AddField(
            model_name='requisition_product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=purchases.models.get_files_path),
        ),
    ]
