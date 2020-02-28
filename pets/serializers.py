from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = "__all__"


class SheltingPetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ["name", "photo", "status"]
