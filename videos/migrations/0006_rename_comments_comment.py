# Generated by Django 4.1 on 2022-09-27 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_profile_image_and_more'),
        ('videos', '0005_alter_video_dislike_alter_video_like_comments_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]