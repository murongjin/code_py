# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20180308_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectioninfo',
            name='ssh_pub_key_path',
        ),
        migrations.AlterField(
            model_name='connectioninfo',
            name='auth_type',
            field=models.IntegerField(choices=[(0, 'password'), (1, 'free-key')], default=0),
        ),
    ]
