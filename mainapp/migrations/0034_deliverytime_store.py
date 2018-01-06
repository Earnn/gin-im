# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_deliverytime'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverytime',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Store'),
        ),
    ]
