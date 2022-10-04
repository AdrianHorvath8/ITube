# Generated by Django 4.1 on 2022-10-04 07:44

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(crop=None, default='images/videos_thumbnail/video_thumbnail_default.png', force_format=None, keep_meta=True, quality=-1, scale=0.5, size=[800, 338], upload_to='images/videos_thumbnail/'),
        ),
    ]
