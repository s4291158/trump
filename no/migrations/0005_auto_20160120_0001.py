# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('no', '0004_quote_quote_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_valid',
            field=models.BooleanField(default=True),
        ),
    ]
