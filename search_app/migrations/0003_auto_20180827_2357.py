from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0002_auto_20180827_2055'),
    ]

    operations = [
        TrigramExtension()
    ]
