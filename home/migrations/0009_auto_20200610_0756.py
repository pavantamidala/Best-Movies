# Generated by Django 3.0.7 on 2020-06-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_movie_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Genre',
            field=models.CharField(default='DEFAULT VALUE', max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='Synopsis',
            field=models.CharField(default='DEFAULT VALUE', max_length=400),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(default='DEFAULT VALUE', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Movie_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Production_company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Starring',
            field=models.CharField(max_length=130),
        ),
    ]