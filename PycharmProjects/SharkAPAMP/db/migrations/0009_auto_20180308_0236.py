# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20180308_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleinfo',
            name='module_path',
            field=models.FilePathField(blank=True, null=True, verbose_name='模块路径'),
        ),
    ]
