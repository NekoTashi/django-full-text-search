from django.urls import path

from search_app.views import AuthorSearchUnaccentView
from search_app.views import AuthorSearchTrigramView
from search_app.views import AuthorSearchLookUpView
from search_app.views import AuthorSearchVectorView
from search_app.views import AuthorSearchQueryNotView
from search_app.views import AuthorSearchQueryOrView
from search_app.views import AuthorSearchQueryAndView
from search_app.views import AuthorSearchRankView
from search_app.views import AuthorSearchLenguageConfigView
from search_app.views import AuthorSearchRankWeightView
from search_app.views import AuthorSearchVectorFieldView

urlpatterns = [
    path(
        "authors/unaccent/",
        AuthorSearchUnaccentView.as_view(),
        name="author-unaccent",
    ),
    path(
        "authors/trigram/",
        AuthorSearchTrigramView.as_view(),
        name="author-trigram"
    ),
    path(
        "authors/django-lookup/",
        AuthorSearchLookUpView.as_view(),
        name="author-django-lookup",
    ),
    path(
        "authors/django-search-vector/",
        AuthorSearchVectorView.as_view(),
        name="author-django-search-vector",
    ),
    path(
        "authors/django-search-query-not/",
        AuthorSearchQueryNotView.as_view(),
        name="author-django-search-query-not",
    ),
    path(
        "authors/django-search-query-or/",
        AuthorSearchQueryOrView.as_view(),
        name="author-django-search-query-or",
    ),
    path(
        "authors/django-search-query-and/",
        AuthorSearchQueryAndView.as_view(),
        name="author-django-search-query-and",
    ),
    path(
        "authors/django-search-rank/",
        AuthorSearchRankView.as_view(),
        name="author-django-search-rank",
    ),
    path(
        "authors/django-search-with-lenguage/",
        AuthorSearchLenguageConfigView.as_view(),
        name="author-django-search-with-lenguage",
    ),
    path(
        "authors/django-search-rank-weight/",
        AuthorSearchRankWeightView.as_view(),
        name="author-django-search-rank-weight",
    ),
    path(
        "authors/django-search-vector-field/",
        AuthorSearchVectorFieldView.as_view(),
        name="author-django-search-vector-field",
    ),
]
