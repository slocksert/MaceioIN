from django.db import migrations
from django.contrib.auth import get_user_model
from decouple import config

def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create_superuser(
        email=config('ADMIN_EMAIL'),
        password=config('ADMIN_PASSWORD'),
        username=config('ADMIN_NAME')
    )

class Migration(migrations.Migration):
    
        dependencies = [
            ('base', '0003_remove_user_date_joined_remove_user_is_active_and_more'),
        ]
    
        operations = [
            migrations.RunPython(create_superuser),
        ]