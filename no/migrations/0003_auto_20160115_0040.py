# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('no', '0002_auto_20160114_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvedquote',
            name='quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ApprovedQuote',
        ),
    ]
