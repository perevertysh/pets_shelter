import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models

from pets.models import Pet


class Registration(models.Model):
    """Pet registration information"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name="Дата регистрации")
    cage = models.CharField(max_length=10, verbose_name=_("Номер клетки"))
    reg_num = models.CharField(max_length=256, auto_created=True,
                               null=True, blank=True,
                               verbose_name=_("Регистрационный номер"))

    # pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE,
    #                         verbose_name=_("Питомец"),
    #                         null=False, related_name="registration_pet")

    def __str__(self):
        return self.reg_num if self.reg_num else self.date.strftime("%d-%m-%Y")


class Owner(models.Model):
    """Information about owner"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256, verbose_name=_("Имя"))
    lastname = models.CharField(max_length=256, verbose_name=_("Фамилия"))
    note = models.CharField(max_length=256, verbose_name=_("Описание"))

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class PetShelteringRequest(models.Model):
    """Request for sheltering of pet"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    phone_num = models.CharField(max_length=12,
                                 verbose_name=_("Номер телефона"))
    email = models.EmailField(verbose_name=_("Адрес эл.почты"))
    firstname = models.CharField(max_length=20, verbose_name=_("Имя"))
    middlename = models.CharField(max_length=20, verbose_name=_("Отчество"))
    lastname = models.CharField(max_length=20, verbose_name=_("Фамилия"))
    comment = models.TextField(max_length=500, verbose_name=_("Комментарии"))

    pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE,
                            verbose_name=_("Питомец"),
                            null=True, blank=True,
                            related_name="pet_sheltering_request_pet")

    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.pet}"
