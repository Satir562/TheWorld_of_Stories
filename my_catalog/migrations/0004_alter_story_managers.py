# Generated by Django 5.0.3 on 2024-03-14 10:54

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_catalog', '0003_alter_story_poster'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='story',
            managers=[
                ('obje_imj', django.db.models.manager.Manager()),
            ],
        ),
    ]