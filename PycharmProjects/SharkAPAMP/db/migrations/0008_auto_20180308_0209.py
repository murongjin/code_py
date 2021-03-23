# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_auto_20180307_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='asset',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Asset', verbose_name='对应资产'),
        ),
    ]
