# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='delivery_boundary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
