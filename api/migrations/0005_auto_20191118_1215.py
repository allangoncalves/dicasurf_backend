# Generated by Django 2.2.5 on 2019-11-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191107_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='state',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]