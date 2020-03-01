from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView)

from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import filters

from .models import Pet

from .serializers import PetSerializer, SheltingPetsSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'main.html', {})

from django_filters import rest_framework as df_filters


class BreedViewSet(viewsets.ModelViewSet):
    pass


class PetViewSet(viewsets.ModelViewSet):
    # pagination_class = pagination.PageNumberPagination
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       df_filters.DjangoFilterBackend]
    search_fields = (
        'name', 'age', 'species__name', 'breed__name', 'status__name',)
    filterset_fields = (
        'name', 'age', 'species__name', 'breed__code', 'status__code',)


class SheltingPetsViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = SheltingPetsSerializer
    queryset = Pet.objects.filter(status__code="shelted")
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
