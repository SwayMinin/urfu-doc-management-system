# Generated by Django 4.2.6 on 2023-11-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docflow', '0019_alter_application_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]