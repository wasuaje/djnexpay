# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cbu_number',
            field=models.CharField(max_length=22),
        ),
    ]
