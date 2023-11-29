# Generated by Django 4.2.6 on 2023-11-26 19:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0004_delete_hero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='current_department_id',
            new_name='current_department',
        ),
        migrations.AlterField(
            model_name='application',
            name='student_education_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docflow.educationlevel'),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_passport',
            field=models.TextField(max_length=10, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]