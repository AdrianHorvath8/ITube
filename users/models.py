from django.db import models
#from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_resized import ResizedImageField

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, channel_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email = self.normalize_email(email),
            channel_name = channel_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, channel_name, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email, password, channel_name, password, **extra_fields)

    
    def create_superuser(self, email, password, channel_name, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email, password, channel_name, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    channel_name = models.CharField(max_length=240)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["channel_name"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"




class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    channel_name = models.CharField(max_length=150, null=True, blank=True, unique=True)
    profile_image = models.ImageField(null=False, blank=False, upload_to="images/profiles/", default="images/profiles/user-default.png")
    profile_thumbnail = ResizedImageField(size=[1036, 256], crop=['middle', 'center'],null=False, blank=False, upload_to="images/profiles_thumbnail/", default="images/profiles_thumbnail/profile_thumbnail_default.png")
    private_list = models.ForeignKey("videos.Video", on_delete=models.SET_NULL, related_name="private" , null=True, blank=True)
    public_list = models.ForeignKey("videos.Video", on_delete=models.SET_NULL, related_name="public" , null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True, unique=True)
    short_info = models.CharField(max_length=200, null=True, blank=True)
    following = models.ManyToManyField(MyUser,related_name="following", blank=True)
    followers = models.ManyToManyField(MyUser,related_name="followers", blank=True)
    history = models.ManyToManyField("videos.Video", blank=True, related_name="history")
    favorite_video = models.ManyToManyField("videos.Video", blank=True)
    facebook_link = models.CharField(max_length=1000, null=True, blank=True)
    instagram_link = models.CharField(max_length=1000, null=True, blank=True)
    twitter_link = models.CharField(max_length=1000, null=True, blank=True)
    spotify_link = models.CharField(max_length=1000, null=True, blank=True)
    itunes_link = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.channel_name)

    @property
    def count_followers(self):
        return self.followers.count()



class Bell(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ManyToManyField(Profile, blank=True, related_name="profiles")

    def __str__(self):
        return str(self.profile)
