from rest_framework import viewsets
from rest_framework import pagination

from .models import (Owner,
                     PetShelteringRequest,
                     Registration)

from .serializers import (OwnerSerializer,
                          PetShelteringRequestSerializer,
                          RegistrationSerializer)


class OwnerViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all().order_by("lastname")


class PetShelteringRequestViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = PetShelteringRequestSerializer
    queryset = PetShelteringRequest.objects.all().order_by("lastname")


class RegistrationViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all().order_by("-date")
