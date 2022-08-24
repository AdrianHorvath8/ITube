

from .models import Profile, MyUser
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver



@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user = user,
            channel_name = user.channel_name,
            email = user.email

        )
        profile.save()



@receiver(post_delete, sender=Profile)
def delete_user(sender, instance,**kwargs):
    user = instance.user
    user.delete()