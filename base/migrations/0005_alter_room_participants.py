# Generated by Django 4.0 on 2021-12-23 15:43

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_alter_message_options_alter_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, default=django.contrib.auth.models.User, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
