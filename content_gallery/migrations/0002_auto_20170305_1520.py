# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
