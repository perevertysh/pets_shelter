from django.urls import include, path

from .views import (PetViewSet)

routes =[
    (r'petslist', PetViewSet),
]

urlpatterns = [ ]