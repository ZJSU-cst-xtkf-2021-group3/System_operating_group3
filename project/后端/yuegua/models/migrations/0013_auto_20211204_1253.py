# Generated by Django 3.2.9 on 2021-12-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_star'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollow_topic',
            name='AgeRange',
        ),
        migrations.AlterField(
            model_name='userfollow_topic',
            name='FTID',
            field=models.IntegerField(verbose_name='被关注话题的ID'),
        ),
    ]
