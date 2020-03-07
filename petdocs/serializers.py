import re

from rest_framework import serializers

from .models import (Owner, PetShelteringRequest, Registration)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields ="__all__"


class PetShelteringRequestSerializer(serializers.ModelSerializer):

    def validate_phone_num(self, value):
        if len(re.findall(r"(\+7\d{10})", value)) != 1:
           raise serializers.ValidationError("Номер должен соответствовать "
                             "+79********* !")
        return value

    class Meta:
        model = PetShelteringRequest
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields ="__all__"
