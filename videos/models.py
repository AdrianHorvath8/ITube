
from email.policy import default
from tkinter import Image
from django.db import models
import uuid

from django_resized import ResizedImageField

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    name = models.TextField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.ForeignKey("users.Profile", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=200)
    body = models.FileField(upload_to="videos", null=True, blank=True)
    thumbnail = ResizedImageField(size=[600, 338], crop=['middle', 'center'],null=False, blank=False, upload_to="images/videos_thumbnail/", default="images/videos_thumbnail/video_thumbnail_default.png")
    views = models.ManyToManyField("users.Profile", blank=True, related_name="views")
    like = models.ManyToManyField("users.Profile", blank=True, related_name="likes")
    dislike = models.ManyToManyField("users.Profile", blank=True, related_name="dislikes")
    description = models.TextField(blank=True, null=True, max_length= 500)
    tag = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    owner = models.ForeignKey("users.Profile", on_delete=models.SET_NULL, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    body = models.CharField(blank=True, null=True, max_length=500)
    heart = models.BooleanField(default=False)
    like = models.ManyToManyField("users.Profile", blank=True, related_name="like")
    dislike = models.ManyToManyField("users.Profile", blank=True, related_name="dislike")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body