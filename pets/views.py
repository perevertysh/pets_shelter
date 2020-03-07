from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView)

from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import filters

from .models import (Pet, Breed, PetStatus, Species, Gender)
from .serializers import (PetSerializer, ShelteringPetsSerializer,
                          BreedSerializer, PetStatusSerializer,
                          SpeciesSerializer, GenderSerializer)


def home(request):
    return render(request, 'main.html', {})


from django_filters import rest_framework as df_filters


class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class PetStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PetStatusSerializer
    queryset = PetStatus.objects.all()


class SpeciesViewSet(viewsets.ModelViewSet):
    serializer_class = SpeciesSerializer
    queryset = Species.objects.all()


class GenderViewSet(viewsets.ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class PetViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = PetSerializer
    queryset = Pet.objects.all().order_by("doc__date")
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       df_filters.DjangoFilterBackend]
    search_fields = (
        'name', 'age', 'species__name', 'gender__name',)
    filterset_fields = (
        'name', 'age', 'species__name', 'breed__code', 'gender__code',
        'status__code',)


class SheltingPetsViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = ShelteringPetsSerializer
    queryset = Pet.objects.filter(status__code="shelted")
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
