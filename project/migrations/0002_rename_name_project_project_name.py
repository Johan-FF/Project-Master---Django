# Generated by Django 4.1.13 on 2024-05-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
    ]