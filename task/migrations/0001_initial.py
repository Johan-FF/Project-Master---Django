# Generated by Django 4.1.13 on 2024-05-21 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Comments', models.TextField()),
                ('delivery_date', models.DateField()),
                ('state', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completada', 'Completada')], max_length=50)),
                ('empleado_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to='employee.employee')),
            ],
        ),
    ]
