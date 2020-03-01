from django.urls import include, path

from .views import (IndexPageView,
                    PetListView,
                    ContactsView,
                    PetView,
                    PetViewSet,
                    BreedViewSet,
                    PetStatusViewSet,
                    SpeciesViewSet)

routes = [
    (r'petslist', PetViewSet),
    (r'breed', BreedViewSet),
    (r'pet_status', PetStatusViewSet),
    (r'species', SpeciesViewSet)
]

urlpatterns = [
    # path('pets/', PetListView.as_view()),
    # path('pets/<str:pk>/', PetView.as_view()),
    # path('contacts/', ContactsView.as_view()),
]
