from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, WorkerPorfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if hasattr(instance, 'inn'):
            WorkerPorfile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email, inn=instance.inn, city=instance.city)
        else:
            instance.save()
            UserProfile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)

# @receiver(post_save, sender=UserProfile)
# def update_username(sender, instance, **kwargs):
#     user = User.objects.get(id=instance.user_id)
#     user.username = instance.username
#     user.first_name = instance.first_name
#     user.save()

# @receiver(post_save, sender=WorkerPorfile)
# def update_username(sender, instance, **kwargs):
#     user = User.objects.get(id=instance.user_id)
#     user.username = instance.username
#     user.first_name = instance.first_name
#     user.inn 
#     user.save()