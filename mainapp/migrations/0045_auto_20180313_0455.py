# Generated by Django 2.0.1 on 2018-03-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0044_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='created_by',
        ),
        migrations.AddField(
            model_name='store',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
