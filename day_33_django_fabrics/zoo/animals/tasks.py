from time import sleep

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def new_animal_created_notification(name: str, created_at: str, path: str):
    print("Start sending email...")
    sleep(5)
    send_mail(
        # subject
        f"New Animal created: {name!r}",
        # text
        (
            f"At {created_at} new animal {name!r} was created!"
            "\n\n"
            f"Check the animal: {settings.BASE_URL}{path}"
        ),
        # from
        "admin@example.com",
        # to
        ["manager@example.com"],
        fail_silently=True,
    )

    print("Sent email.")
