# Generated by Django 3.2.9 on 2021-12-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_comments_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='hotPoints',
            field=models.FloatField(default=0.0, verbose_name='热门指数'),
        ),
    ]
