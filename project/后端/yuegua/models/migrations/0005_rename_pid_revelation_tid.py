# Generated by Django 3.2.9 on 2021-12-01 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_user_ifpassedexam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revelation',
            old_name='PID',
            new_name='TID',
        ),
    ]
