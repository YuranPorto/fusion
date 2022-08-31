# Generated by Django 4.1 on 2022-08-31 20:27

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=pictures.models.PictureField(aspect_ratios=['1/1'], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['PNG', 'JPEG'], grid_columns=12, pixel_densities=[1, 2], upload_to='equipe', verbose_name='Imagem'),
        ),
    ]
