# Generated by Django 4.1 on 2022-08-31 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(upload_to='equipe', verbose_name='Imagem'),
        ),
    ]
