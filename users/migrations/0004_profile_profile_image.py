# Generated by Django 4.1 on 2022-08-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_followers_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profiles/user-default.png', upload_to='profiles/'),
        ),
    ]
