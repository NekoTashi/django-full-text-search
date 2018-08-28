from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    lang = models.CharField(max_length=100, default="english")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.name
