# Generated by Django 2.2.5 on 2019-12-19 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitemanager', '0006_sphereimage'),
        ('api', '0014_imagepanel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_five', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_five', to='sitemanager.SphereImage', verbose_name='Imagem 5')),
                ('image_four', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_four', to='sitemanager.SphereImage', verbose_name='Imagem 4')),
                ('image_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_one', to='sitemanager.SphereImage', verbose_name='Imagem 1')),
                ('image_six', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_six', to='sitemanager.SphereImage', verbose_name='Imagem 6')),
                ('image_three', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_three', to='sitemanager.SphereImage', verbose_name='Imagem 3')),
                ('image_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_two', to='sitemanager.SphereImage', verbose_name='Imagem 2')),
            ],
            options={
                'verbose_name': 'Grids',
                'verbose_name_plural': 'Grid 360',
            },
        ),
        migrations.RemoveField(
            model_name='spotdetail',
            name='info_image',
        ),
        migrations.AlterField(
            model_name='city',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Visivel para todo o site'),
        ),
        migrations.AlterField(
            model_name='state',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Visivel para todo o site'),
        ),
        migrations.DeleteModel(
            name='ImagePanel',
        ),
        migrations.AddField(
            model_name='imagegrid',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_panel', to='api.SpotDetail', verbose_name='Painel de Imagens'),
        ),
    ]
