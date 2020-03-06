from django.contrib import admin
from django.forms import ModelForm

from .models import Registration, Owner, PetShelteringRequest


class RegistrationForm(ModelForm):
    pass


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    """Регистрационные документы"""
    exclude = ["reg_num"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Владелец питомца"""


@admin.register(PetShelteringRequest)
class PetShelteringRequestAdmin(admin.ModelAdmin):
    """Владелец питомца"""
