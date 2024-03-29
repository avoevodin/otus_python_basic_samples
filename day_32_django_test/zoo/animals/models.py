from django.conf import settings
from django.contrib import admin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from .tasks import new_animal_created_notification


class AnimalKind(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField(null=True)
    kind = models.ForeignKey(AnimalKind, on_delete=models.PROTECT, null=True)
    description = models.TextField(blank=True, null=False)
    food = models.ManyToManyField("animals.AnimalFood", related_name="animals")
    created_at = models.DateTimeField(auto_created=True)

    @property
    @admin.display(description="Created at")
    def created_at_str(self):
        return self.created_at.isoformat(sep=" ", timespec="minutes")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Animal #{self.pk} {self.name!r}>"


class AnimalDetail(models.Model):
    animal = models.OneToOneField(
        Animal,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="details",
    )
    biography = models.TextField(blank=True)

    # @property
    # def bio_short(self):
    #     return self.biography[:50]

    def __str__(self):
        return self.biography


class AnimalFood(models.Model):
    class Meta:
        verbose_name_plural = "Animal food"

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


@receiver(post_save, sender=Animal)
def animal_saved_handler(instance: Animal, created: bool, **kwargs):
    # print(f"instance: {instance}, created: {created}")
    if not created:
        return

    if not settings.SEND_EMAIL_NOTIFICATION:
        return

    path = reverse("animals:details", kwargs=dict(pk=instance.pk))
    task = new_animal_created_notification.delay(
        instance.name, instance.created_at_str, path
    )
    print(task, repr(task.id), repr(task.backend))
