# Generated by Django 4.2 on 2023-04-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='isPublished',
            new_name='is_published',
        ),
    ]
