import uuid

from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.urls import reverse


class Gender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Пол")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Порода")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Species(models.Model):
    """Species of pet"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Вид животного")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class PetStatus(models.Model):
    """pet's sheltering status"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Статус питомца")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Pet(models.Model):
    """Main pet description"""
    """
    - питомец:
        - кличка
        - возраст
        - пол
        (от до (интервалы))
        - привит, не прививки
    - более подробный профиль питомца
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="Кличка")
    age = models.IntegerField(verbose_name="Возраст",
                              validators=[validators.MinValueValidator(0),
                                          validators.MaxValueValidator(100)])
    doc = models.ForeignKey('petdocs.Registration', on_delete=models.CASCADE,
                            verbose_name="Регистрационный документ",
                            related_name="pet_registration")
    photo = models.ImageField(upload_to="img", blank=True,
                              verbose_name=_("Фото"))
    species = models.ForeignKey('pets.Species', on_delete=models.CASCADE,
                                verbose_name="Вид животного")
    breed = models.ForeignKey('pets.Breed', on_delete=models.CASCADE,
                              verbose_name="Порода")
    owner = models.ForeignKey("petdocs.Owner", on_delete=models.CASCADE,
                              verbose_name="Владелец", blank=True, null=True)
    status = models.ForeignKey("pets.PetStatus",
                               on_delete=models.CASCADE,
                               verbose_name="Статус питомца", blank=True,
                               null=True)
    gender = models.ForeignKey('pets.Gender', on_delete=models.CASCADE,
                               verbose_name="Пол")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.doc.reg_num = self.breed.name[0] + self.doc.date.strftime(
            "%d%m%Y")
        self.doc.save()
        super().save()

    def make_word_end(self):
        word = "лет"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.breed,
                                    self.make_word_end())

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pk': self.pk})
