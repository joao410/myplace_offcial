# Generated by Django 3.0.11 on 2021-07-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20210723_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_human_resources',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='models_rh/'),
        ),
        migrations.AlterField(
            model_name='report_human_resources',
            name='file_category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='category'),
        ),
    ]