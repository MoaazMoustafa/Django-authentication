# Generated by Django 3.2.9 on 2021-11-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211112_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(to='movies.Category'),
        ),
        migrations.AddField(
            model_name='series',
            name='categories',
            field=models.ManyToManyField(to='movies.Category'),
        ),
    ]
