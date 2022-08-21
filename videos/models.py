
from django.db import models
import uuid


class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)
    title = models.CharField(blank=True, null=True)
    #body = models.FileField(upload_to=)
    #views = models.ManyToManyField(Profile)
    #like = models.ManyToManyField(Profile)
    #dislike = models.ManyToManyField(Profile)
    #comments = models.ForeignKey(Comments)
    description = models.TextField(blank=True, null=True, max_length= 500)
    #tag = models.ManyToManyField(Profile)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title