# Generated by Django 3.2.10 on 2021-12-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_imovel_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='categoria',
            field=models.CharField(choices=[('Apartamento', 'Apartamento'), ('Casa', 'Casa'), ('Destaque', 'Destaque')], max_length=100),
        ),
    ]