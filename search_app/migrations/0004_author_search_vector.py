# Generated by Django 2.1 on 2018-08-28 21:02

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0003_auto_20180827_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
