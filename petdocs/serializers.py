from rest_framework import serializers

from .models import PetShelteringRequest


class PetShelteringRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetShelteringRequest
        fields = "__all__"
