# Generated by Django 5.1.3 on 2024-11-13 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='imporancia',
            new_name='importante',
        ),
    ]
