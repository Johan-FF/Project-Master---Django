# Generated by Django 4.1.13 on 2024-05-21 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
                ('employees_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('id_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.contactorganization')),
            ],
        ),
    ]
