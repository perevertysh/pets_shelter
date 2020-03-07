from django.urls import include, path

from .views import (home,
                    PetViewSet,
                    BreedViewSet,
                    PetStatusViewSet,
                    SpeciesViewSet,
                    GenderViewSet)

routes = [
    (r'pet', PetViewSet),
    (r'breed', BreedViewSet),
    (r'pet_status', PetStatusViewSet),
    (r'species', SpeciesViewSet),
    (r'gender', GenderViewSet)
]

urlpatterns = []
