# Generated by Django 5.2.1 on 2025-05-20 16:07

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_userprofile_is_guest_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dfcon4lff/image/upload/v1747749458/tlnjhjrdeqdjfyxxn9as.png', max_length=255, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default="Hi i'm new here"),
        ),
    ]
