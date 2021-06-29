# Generated by Django 3.2.4 on 2021-06-28 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('amount', models.IntegerField(blank=True, default=0, verbose_name='quantidade')),
                ('category_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='cod_categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('brand', models.CharField(max_length=254, verbose_name='marca')),
                ('model', models.CharField(max_length=100, verbose_name='modelo')),
                ('amount', models.IntegerField(blank=True, default=0, verbose_name='quantidade_produto')),
                ('product_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='cod_produto')),
                ('category_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('part_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='codigo da peça')),
                ('defect', models.BooleanField(default=False)),
                ('used', models.BooleanField(default=False)),
                ('associate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
            options={
                'verbose_name': 'Peça',
                'verbose_name_plural': 'Peças',
            },
        ),
        migrations.CreateModel(
            name='Log_entrance',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('entrance_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='codigo da entrada')),
                ('amount', models.IntegerField(default=0, verbose_name='quantidade')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('part_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.product_details')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.product')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='Log_defect',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('defect_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='codigo do defeito')),
                ('reason', models.CharField(max_length=255, verbose_name='motivo')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('part_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.product_details')),
            ],
            options={
                'verbose_name': 'Defeito',
                'verbose_name_plural': 'Defeitos',
            },
        ),
        migrations.CreateModel(
            name='Log_association',
            fields=[
                ('create', models.DateField(auto_now_add=True, verbose_name='Criacao')),
                ('update', models.DateField(auto_now=True, verbose_name='Atualizacao')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('association_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='codigo da Associação')),
                ('creator', models.CharField(max_length=255, verbose_name='criador')),
                ('action', models.CharField(max_length=100, verbose_name='Ação')),
                ('associate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('part_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.product_details')),
            ],
            options={
                'verbose_name': 'Associação',
                'verbose_name_plural': 'Associações',
            },
        ),
    ]
