# Generated by Django 3.1.3 on 2020-11-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100', '0003_remove_album_descripcionalbum'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='descripcionAlbum',
            field=models.TextField(null=True),
        ),
    ]
