# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_auto_20180107_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverytime',
            old_name='friday_off',
            new_name='friday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='monday_off',
            new_name='monday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='saturday_off',
            new_name='saturday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='sunday_off',
            new_name='sunday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='thursday_off',
            new_name='thursday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='tuesday_off',
            new_name='tuesday',
        ),
        migrations.RenameField(
            model_name='deliverytime',
            old_name='wednesday_off',
            new_name='wednesday',
        ),
    ]