# Generated by Django 2.2.3 on 2019-09-19 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190919_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=30, verbose_name='Sexo'),
        ),
    ]
