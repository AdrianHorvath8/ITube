

from .models import Profile, MyUser, Bell
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings



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

        bell = Bell.objects.create(
            owner = profile
        )
        bell.save()



        subject = "ITube Team"
        message = "Thank you for registration to best startup project in the world <3"


        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )



@receiver(post_delete, sender=Profile)
def delete_user(sender, instance,**kwargs):
    user = instance.user
    user.delete()