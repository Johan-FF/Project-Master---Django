# Generated by Django 4.1.13 on 2024-05-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_remove_organization_id_contact_organization_admin_and_more'),
        ('role', '0003_alter_role_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='role_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
    ]
