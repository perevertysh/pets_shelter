from rest_framework import serializers

from .models import (Owner, PetShelteringRequest, Registration)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields ="__all__"


class PetShelteringRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetShelteringRequest
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields ="__all__"
