# Generated by Django 4.1 on 2022-10-04 07:42

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_remove_video_thumbnnail_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(crop=None, default='images/videos_thumbnail/video_thumbnail_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[800, 338], upload_to='images/videos_thumbnail/'),
        ),
    ]
