# Generated by Django 3.2.10 on 2021-12-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_imovel_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('ID_Depoimentos', models.AutoField(primary_key=True, serialize=False)),
                ('imageDep', models.ImageField(upload_to='img_Depoimentos/%y')),
                ('nome_depoente', models.CharField(max_length=100)),
                ('cliente_Dep', models.CharField(max_length=200)),
            ],
        ),
    ]
