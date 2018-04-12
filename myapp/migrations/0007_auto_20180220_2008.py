# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_articulo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(default='-', unique=True),
            preserve_default=False,
        ),
    ]
