# Generated by Django 2.2.5 on 2019-09-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190927_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_text',
            field=models.CharField(max_length=250),
        ),
    ]
