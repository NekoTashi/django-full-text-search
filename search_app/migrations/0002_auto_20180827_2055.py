from django.db import migrations
from django.contrib.postgres.operations import UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        UnaccentExtension(),
    ]
