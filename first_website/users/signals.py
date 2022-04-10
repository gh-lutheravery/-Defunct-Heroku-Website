from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# User sends itself over to the reciever decoration. post_save is the signal that is sent after the User is saved.
# create_profile is the reciever function, that takes in multiple arguments. instance is the User instance, and created
# tells if its been created or not.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
