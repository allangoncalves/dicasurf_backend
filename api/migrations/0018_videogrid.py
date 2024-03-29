# Generated by Django 2.2.5 on 2019-12-19 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0007_spherevideo'),
        ('api', '0017_auto_20191219_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_panel', to='api.SpotDetail', verbose_name='Pico')),
                ('video_five', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_five', to='sitemanager.SphereVideo', verbose_name='Video 5')),
                ('video_four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_four', to='sitemanager.SphereVideo', verbose_name='Video 4')),
                ('video_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_one', to='sitemanager.SphereVideo', verbose_name='Video 1')),
                ('video_six', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_six', to='sitemanager.SphereVideo', verbose_name='Video 6')),
                ('video_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_three', to='sitemanager.SphereVideo', verbose_name='Video 3')),
                ('video_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='video_two', to='sitemanager.SphereVideo', verbose_name='Video 2')),
            ],
            options={
                'verbose_name': 'Grid 360 (Video)',
                'verbose_name_plural': 'Grids (Video)',
            },
        ),
    ]
