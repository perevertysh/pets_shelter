from rest_framework import viewsets
from rest_framework import pagination


from .models import PetShelteringRequest

from .serializers import PetShelteringRequestSerializer


class PetShelteringRequestViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = PetShelteringRequestSerializer
    queryset = PetShelteringRequest.objects.all()
