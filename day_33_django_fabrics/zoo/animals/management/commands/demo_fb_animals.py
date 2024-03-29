import factory
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory


class AnimalKindFactory(DjangoModelFactory):
    class Meta:
        model = "animals.AnimalKind"

    name = factory.Faker("word", locale="ru_RU")


class Command(BaseCommand):
    def handle(self, *args, **options):
        kind = AnimalKindFactory.build()
        print(kind)
        print(vars(kind))

        kind = AnimalKindFactory.create()
        print(kind)
        print(vars(kind))
