# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-20 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171218_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denominacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='denominacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Denominacion'),
        ),
    ]
