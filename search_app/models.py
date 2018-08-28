from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.name
