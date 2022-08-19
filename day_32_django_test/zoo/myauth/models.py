from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel: AbstractUser = get_user_model()
# print("user model: ", UserModel, "repr: ", repr(UserModel))


# class MyCustomUser(AbstractUser):
#     pass


class UserProfile(models.Model):
    # user = models.OneToOneField('myauth.MyCustomUser')
    # user = models.OneToOneField(settings.AUTH_USER_MODEL)
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(null=False, blank=True)


@receiver(post_save, sender=UserModel)
def user_saved_handler(instance: UserModel, created: bool, **kwargs):
    print(f"instance: {instance}, created: {created}")
    if not created:
        return

    UserProfile.objects.create(user=instance)
