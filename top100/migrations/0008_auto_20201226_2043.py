# Generated by Django 3.1.1 on 2020-12-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100', '0007_estilo_descripcionestilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='imagenArtista',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]
