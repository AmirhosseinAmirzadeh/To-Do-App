# Generated by Django 4.2.19 on 2025-03-04 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Due_time',
            new_name='due_time',
        ),
    ]
