from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView)

from rest_framework import viewsets
from rest_framework import pagination

from .models import Pet

from .serializers import PetSerializer, SheltingPetsSerializer


class IndexPageView(TemplateView):

    template_name = 'index.html'


class PetListView(ListView):

    model = Pet

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        # search
        if get_params.get('q'):
            qs = qs.filter(name__icontains=get_params.get('q'))

        return qs


class PetView(DetailView):

    model = Pet


class ContactsView(TemplateView):

    template_name = 'contacts.html'


class PetViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


class SheltingPetsViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = SheltingPetsSerializer
    queryset = Pet.objects.filter(status__code="shelted")