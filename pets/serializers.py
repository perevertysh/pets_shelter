from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from petdocs.models import Owner, Registration
from .models import Pet, Breed, Species, PetStatus


class PetSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(),
        required=False,
        allow_empty=True,
        label=_("Порода"))
    species = serializers.PrimaryKeyRelatedField(
        queryset=Species.objects.all(),
        required=False, allow_empty=True,
        label=_("Вид животного"))
    pet_status = serializers.PrimaryKeyRelatedField(
        queryset=PetStatus.objects.all(),
        required=False,
        allow_empty=True,
        label=_("Статус"))
    doc = serializers.PrimaryKeyRelatedField(
        queryset=Registration.objects.all(), required=False,
        allow_empty=True,
        label=_("Статус"))
    owner = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(),
        required=False,
        allow_empty=True,
        label=_("Порода"))

    class Meta:
        model = Pet
        fields = "__all__"


class SheltingPetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["name", "photo", "status"]
