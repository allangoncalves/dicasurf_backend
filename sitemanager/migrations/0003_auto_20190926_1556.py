# Generated by Django 2.2.5 on 2019-09-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0002_auto_20190925_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='first_carousel_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title',
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='sitemanager.HomePage')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Carousel',
            },
        ),
    ]