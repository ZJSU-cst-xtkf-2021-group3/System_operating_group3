# Generated by Django 3.2.9 on 2021-12-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_auto_20211204_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic_vote',
            name='counts',
            field=models.IntegerField(default=0, verbose_name='计数'),
        ),
    ]
