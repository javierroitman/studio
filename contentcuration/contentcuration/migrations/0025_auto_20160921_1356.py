# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0024_auto_20160920_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentitem',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
