from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchQuery
from django.contrib.postgres.search import SearchRank

from rest_framework.views import APIView
from rest_framework.response import Response

from search_app.models import Author


class AuthorSearchUnaccentView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names ignoring accent.
        """
        search_value = request.query_params.get("search")

        names = Author.objects.filter(name__unaccent=search_value).values_list(
            "name", flat=True
        )

        return Response(names)


class AuthorSearchTrigramView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using trigram similarity algorithm.
        """
        search_value = request.query_params.get("search")

        names = Author.objects.filter(name__trigram_similar=search_value).values_list(
            "name", flat=True
        )

        return Response(names)


class AuthorSearchLookUpView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django lookup full text search.
        """
        search_value = request.query_params.get("search")

        names = Author.objects.filter(name__trigram_similar=search_value).values_list(
            "name", flat=True
        )

        return Response(names)


class AuthorSearchVectorView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django search vector.
        """
        search_value = request.query_params.get("search")

        search_vector = SearchVector("name", "email")
        names = (
            Author.objects.annotate(search=search_vector)
            .filter(search=search_value)
            .values_list("name", flat=True)
        )

        return Response(names)


class AuthorSearchQueryNotView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django NOT search query.
        """
        search_value = request.query_params.get("search")

        search_query = ~SearchQuery(search_value)
        search_vector = SearchVector("name")
        names = (
            Author.objects.annotate(search=search_vector)
            .filter(search=search_query)
            .values_list("name", flat=True)
        )

        return Response(names)


class AuthorSearchQueryOrView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django NOT search query.
        """
        search_value_1 = request.query_params.get("search_1")
        search_value_2 = request.query_params.get("search_2")

        search_query = SearchQuery(search_value_1) | SearchQuery(search_value_2)
        search_vector = SearchVector("name")
        names = (
            Author.objects.annotate(search=search_vector)
            .filter(search=search_query)
            .values_list("name", flat=True)
        )

        return Response(names)


class AuthorSearchQueryAndView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django AND search query.
        """
        search_value_1 = request.query_params.get("search_1")
        search_value_2 = request.query_params.get("search_2")

        search_query = SearchQuery(search_value_1) & SearchQuery(search_value_2)
        search_vector = SearchVector("name")
        names = (
            Author.objects.annotate(search=search_vector)
            .filter(search=search_query)
            .values_list("name", flat=True)
        )

        return Response(names)


class AuthorSearchRankView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django search rank.
        """
        search_value = request.query_params.get("search")

        search_vector = SearchVector("name")
        search_query = SearchQuery(search_value)
        search_rank = SearchRank(search_vector, search_query)

        authors = (
            Author.objects.annotate(rank=search_rank)
            .order_by("-rank")
            .values_list("name", "rank")
        )

        return Response(authors)


class AuthorSearchLenguageConfigView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django search rank with lenguage config.
        """
        lenguage = "english"
        search_value = request.query_params.get("search")

        search_vector = SearchVector("name", config=lenguage)
        search_query = SearchQuery(search_value, config=lenguage)

        names = (
            Author.objects.annotate(search=search_vector)
            .filter(search=search_query)
            .values_list("name", flat=True)
        )

        return Response(names)


class AuthorSearchRankWeightView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django search rank using weight.
        """
        search_value = request.query_params.get("search")

        search_vector_a = SearchVector("name", weight="A")
        search_vector_b = SearchVector("email", weight="B")

        search_vector = search_vector_a + search_vector_b
        search_query = SearchQuery(search_value)
        search_rank = SearchRank(search_vector, search_query)

        authors = (
            Author.objects.annotate(rank=search_rank)
            .order_by("-rank")
            .values_list("name", "rank")
        )

        return Response(authors)


class AuthorSearchVectorFieldView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Get all author names using django search vector field.
        """
        search_value = request.query_params.get("search")

        names = (
            Author.objects
            .filter(search_vector=search_value)
            .values_list("name", flat=True)
        )

        return Response(names)
