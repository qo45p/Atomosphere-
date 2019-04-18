# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0011_userhealthrecord_painkiller'),
    ]

    operations = [
        migrations.CreateModel(
            name='lonLatData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=5)),
                ('town', models.CharField(max_length=5)),
                ('code', models.PositiveSmallIntegerField()),
                ('lon', models.DecimalField(decimal_places=7, max_digits=11)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='weatherPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=10)),
            ],
        ),
    ]