# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0012_lonlatdata_weatherpicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhealthrecord',
            name='createDate',
        ),
        migrations.RemoveField(
            model_name='userhealthrecord',
            name='endLoginDate',
        ),
    ]
