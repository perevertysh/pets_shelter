from django.urls import include, path

from .views import (PetViewSet,
                    BreedViewSet,
                    PetStatusViewSet,
                    SpeciesViewSet)

routes = [
    (r'petslist', PetViewSet),
    (r'breed', BreedViewSet),
    (r'pet_status', PetStatusViewSet),
    (r'species', SpeciesViewSet)
]

urlpatterns = [ ]

