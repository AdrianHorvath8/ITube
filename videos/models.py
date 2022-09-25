
from django.db import models
import uuid


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
    #body = models.FileField(upload_to=)
    thumbnnail = models.ImageField(null=False, blank=False, upload_to="videos_thumbnail/", default="videos_thumbnail/video_thumbnail_default.png")
    views = models.ManyToManyField("users.Profile", blank=True, related_name="views")
    like = models.ManyToManyField("users.Profile", blank=True, related_name="like")
    dislike = models.ManyToManyField("users.Profile", blank=True, related_name="dislike")
    #comments = models.ForeignKey(Comments)
    description = models.TextField(blank=True, null=True, max_length= 500)
    tag = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title