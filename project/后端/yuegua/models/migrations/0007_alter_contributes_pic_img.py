# Generated by Django 3.2.9 on 2021-12-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_rename_eid_revelation_pic_rid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributes_pic',
            name='img',
            field=models.ImageField(default='/static/img/default.png', upload_to='tougao', verbose_name='活动投稿图片'),
        ),
    ]
