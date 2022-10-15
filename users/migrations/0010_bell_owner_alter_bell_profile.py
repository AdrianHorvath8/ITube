# Generated by Django 4.1 on 2022-10-15 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_bell'),
    ]

    operations = [
        migrations.AddField(
            model_name='bell',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='bell',
            name='profile',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='users.profile'),
        ),
    ]
