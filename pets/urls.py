from django.urls import include, path

from .views import (IndexPageView, PetListView, ContactsView, PetView, PetViewSet)

routes =[
    (r'petslist', PetViewSet),
]

urlpatterns = [
    path('pets/', PetListView.as_view()),
    path('pets/<str:pk>/', PetView.as_view()),
    path('contacts/', ContactsView.as_view()),
]