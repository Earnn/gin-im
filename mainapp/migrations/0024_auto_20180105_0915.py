# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_merge_20180105_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slip_payment',
            field=models.ImageField(blank=True, null=True, upload_to='slip_payment/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='store',
            name='delivery_payment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
