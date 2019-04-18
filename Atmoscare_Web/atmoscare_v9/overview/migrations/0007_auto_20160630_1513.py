# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0006_auto_20160630_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhealthrecord',
            name='AF',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='Asthma',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='DM',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='DysLip',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='HF',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='HT',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='userhealthrecord',
            name='Stroke',
            field=models.BooleanField(default=0),
        ),
    ]
