# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-22 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171222_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
