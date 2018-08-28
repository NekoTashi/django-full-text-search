from django.contrib.postgres.search import SearchVector
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from search_app.models import Author


class AuthorSearchUnaccentViewTest(APITestCase):
    url = reverse("author-unaccent")

    def setUp(self):
        self.author = Author.objects.create(name="Hélèèn", email="helen@gmail.com")

    def test_list_author_names(self):
        name_searched = "Heleen"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.author.name, response.data[0])


class AuthorSearchTrigramViewTest(APITestCase):
    url = reverse("author-trigram")

    def setUp(self):
        self.author = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "chrstopher r"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.author.name, response.data[0])


class AuthorSearchLookUpViewTest(APITestCase):
    url = reverse("author-django-lookup")

    def setUp(self):
        self.author = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "christoph"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.author.name, response.data[0])


class AuthorSearchVectorViewTest(APITestCase):
    url = reverse("author-django-search-vector")

    def setUp(self):
        self.author = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "christoph"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.author.name, response.data[0])


class AuthorSearchQueryNotViewTest(APITestCase):
    url = reverse("author-django-search-query-not")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="felipe@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "christoph"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertFalse(self.author_1.name in response.data)


class AuthorSearchQueryOrViewTest(APITestCase):
    url = reverse("author-django-search-query-or")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="felipe@gmail.com"
        )

    def test_list_author_names(self):
        name_searched_1 = "christoph"
        name_searched_2 = "pedro"

        response = self.client.get(
            self.url + "?search_1=" + name_searched_1 + "&search_2=" + name_searched_2
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.author_1.name in response.data)
        self.assertTrue(self.author_2.name in response.data)


class AuthorSearchQueryAndViewTest(APITestCase):
    url = reverse("author-django-search-query-and")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="felipe@gmail.com"
        )

    def test_list_author_names(self):
        name_searched_1 = "Rubio"
        name_searched_2 = "Christopher"

        response = self.client.get(
            self.url + "?search_1=" + name_searched_1 + "&search_2=" + name_searched_2
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.author_1.name in response.data)


class AuthorSearchRankViewTest(APITestCase):
    url = reverse("author-django-search-rank")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="felipe@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "rubio"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)


class AuthorSearchLenguageConfigViewTest(APITestCase):
    url = reverse("author-django-search-with-lenguage")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="felipe@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "rubio"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.author_1.name in response.data)


class AuthorSearchRankWeightViewTest(APITestCase):
    url = reverse("author-django-search-rank-weight")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="rubio@gmail.com"
        )

    def test_list_author_names(self):
        name_searched = "rubio"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)


class AuthorSearchVectorFieldViewTest(APITestCase):
    url = reverse("author-django-search-vector-field")

    def setUp(self):
        self.author_1 = Author.objects.create(
            name="Christopher Rubio", email="chris@gmail.com"
        )
        self.author_2 = Author.objects.create(
            name="Pedro Quintana", email="pedro@gmail.com"
        )
        self.author_3 = Author.objects.create(
            name="Felipe Rubio", email="rubio@gmail.com"
        )
        Author.objects.update(search_vector=SearchVector("name"))

    def test_list_author_names(self):
        name_searched = "rubio"

        response = self.client.get(self.url + "?search=" + name_searched)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.author_1.name in response.data)
        self.assertTrue(self.author_3.name in response.data)
