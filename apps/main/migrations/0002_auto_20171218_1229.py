# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-18 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='almacen',
            old_name='Piso',
            new_name='piso',
        ),
    ]
