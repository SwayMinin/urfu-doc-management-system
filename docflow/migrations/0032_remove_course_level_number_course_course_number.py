# Generated by Django 4.2.6 on 2023-11-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0031_alter_course_level_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='level_number',
        ),
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(choices=[(1, 'Первый'), (2, 'Второй'), (3, 'Третий'), (4, 'Четвёртый')], default=1),
            preserve_default=False,
        ),
    ]