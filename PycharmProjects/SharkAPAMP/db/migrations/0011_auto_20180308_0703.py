# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20180308_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryhosts',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='db.InventoryGroups', verbose_name='主机组'),
        ),
    ]
