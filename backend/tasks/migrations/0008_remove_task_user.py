# Generated by Django 5.1 on 2024-09-18 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
