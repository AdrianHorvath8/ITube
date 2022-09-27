from django.contrib import admin

from .models import Video, Tag, Comment


admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Comment)