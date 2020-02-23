from django.contrib import admin

from .models import Pet, Breed, Species, PetStatus

admin.site.register(
    (Pet, Breed, Species, PetStatus)
)
