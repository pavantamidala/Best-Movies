# Generated by Django 3.0.7 on 2020-06-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_movie_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
    ]
