# Generated by Django 3.2.9 on 2021-12-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0023_alter_star_typeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='typeID',
        ),
    ]
