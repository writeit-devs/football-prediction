# Generated by Django 4.2 on 2023-05-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0004_alter_notification_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
