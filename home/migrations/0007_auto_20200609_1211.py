# Generated by Django 3.0.7 on 2020-06-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
