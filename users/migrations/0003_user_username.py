# Generated by Django 5.0.4 on 2024-05-10 17:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]