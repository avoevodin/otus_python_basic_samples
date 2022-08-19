from django.core.management import BaseCommand
from faker import Faker

# fake = Faker()
fake = Faker("ru_RU")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(fake.user_name())
        print(fake.email())
        print(fake.pybool())
        print(fake.phone_number())
        print(fake.paragraph())
        print(fake.first_name())
