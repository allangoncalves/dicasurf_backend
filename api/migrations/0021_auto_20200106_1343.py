# Generated by Django 2.2.5 on 2020-01-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20191223_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumb_image',
        ),
        migrations.AlterField(
            model_name='imagegrid',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='videogrid',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nome'),
        ),
    ]
