# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0009_auto_20160630_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhealthrecord',
            name='zipcode',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
