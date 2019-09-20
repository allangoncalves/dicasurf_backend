# Generated by Django 2.2.3 on 2019-09-19 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='news',
            field=models.BooleanField(default=False, verbose_name='Receber notícias'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='terms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Localidade'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(max_length=50, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name='Apelido'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[(0, 'Masculino'), (1, 'Feminino')], max_length=30, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=50, verbose_name='Estado'),
        ),
    ]