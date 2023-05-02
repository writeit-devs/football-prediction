# Generated by Django 4.2 on 2023-05-01 20:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='users',
            field=models.ManyToManyField(default=None, related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
