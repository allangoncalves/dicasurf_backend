# Generated by Django 2.2.5 on 2019-12-12 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0003_partnerpage_partnerslide'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoWeArePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Quem somos',
                'verbose_name_plural': 'Quem somos',
            },
        ),
        migrations.CreateModel(
            name='WhoWeAreSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=255)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='sitemanager.WhoWeArePage')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Carousel',
            },
        ),
    ]