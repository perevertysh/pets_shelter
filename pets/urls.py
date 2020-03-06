from django.urls import include, path

from .views import (home,
                    PetViewSet,
                    BreedViewSet,
                    PetStatusViewSet,
                    SpeciesViewSet)

routes = [
    (r'pet', PetViewSet),
    (r'breed', BreedViewSet),
    (r'pet_status', PetStatusViewSet),
    (r'species', SpeciesViewSet)
]

urlpatterns = []
