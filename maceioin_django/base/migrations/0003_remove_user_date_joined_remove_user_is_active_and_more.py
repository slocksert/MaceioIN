# Generated by Django 5.1.6 on 2025-02-13 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_user_is_staff_remove_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
