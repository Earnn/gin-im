# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20180105_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
