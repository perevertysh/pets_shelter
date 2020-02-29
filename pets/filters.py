from rest_framework import filters
from .models import Breed


class PetBreedFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(breed_id=request.data["breed"])