from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    channel_name = models.CharField(max_length=150, null=True, blank=True, unique=True)
    #profile_image = models.ImageField(null=False, blank=False, upload_to="profiles/", default="profiles/user-default.png")
    #profile_thumbnail = models.ImageField(null=False, blank=False, upload_to="profiles/", default="profiles/user-default.png")
    private_list = models.ForeignKey("videos.Video", on_delete=models.SET_NULL, related_name="private" , null=True, blank=True)
    public_list = models.ForeignKey("videos.Video", on_delete=models.SET_NULL, related_name="public" , null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    short_info = models.CharField(max_length=200, null=True, blank=True)
    followers = models.ManyToManyField(User,related_name="followers", blank=True)
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

