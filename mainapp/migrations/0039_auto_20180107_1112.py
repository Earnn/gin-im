# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 04:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_remove_profile_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='user',
            new_name='created_by',
        ),
    ]
