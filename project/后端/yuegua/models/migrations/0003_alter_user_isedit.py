# Generated by Django 3.2.9 on 2021-11-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20211112_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isEDIT',
            field=models.BooleanField(default=False, verbose_name='是否为编辑'),
        ),
    ]
