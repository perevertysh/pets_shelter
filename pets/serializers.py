from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from petdocs.models import Owner, Registration
from petdocs.serializers import RegistrationSerializer
from .models import Pet, Breed, Species, PetStatus, Gender


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"


class PetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetStatus
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(instance=Breed,
        label=_("Порода"), read_only=True)
        # serializers.PrimaryKeyRelatedField(
        # queryset=Breed.objects.all(),
        # required=False,
        # allow_empty=True,
        # label=_("Порода"))
    species = SpeciesSerializer()
        # serializers.PrimaryKeyRelatedField(
        # queryset=Species.objects.all(),
        # required=False, allow_empty=True,
        # label=_("Вид животного"))
    status = PetStatusSerializer()
        # serializers.PrimaryKeyRelatedField(
        # queryset=PetStatus.objects.all(),
        # required=False,
        # allow_empty=True,
        # label=_("Статус питомца"))
    doc = RegistrationSerializer()
        # serializers.PrimaryKeyRelatedField(
        # queryset=Registration.objects.all(), required=False,
        # allow_empty=True,
        # label=_("Регистрационный документ"))
    owner = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(),
        required=False,
        allow_empty=True,
        label=_("Порода"))
    gender = GenderSerializer()

    class Meta:
        model = Pet
        fields = "__all__"


class SheltingPetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["name", "photo", "status"]
