# Generated by Django 4.1.13 on 2024-05-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_proyecto_aociado_alter_task_empleado_asignado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='task_name',
        ),
    ]
