# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strata', '0006_auto_20170409_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='customer',
            new_name='customers',
        ),
    ]