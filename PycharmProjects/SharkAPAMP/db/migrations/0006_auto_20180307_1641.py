# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20180307_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariableInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, unique=True, verbose_name='变量名')),
                ('values', models.CharField(max_length=255, verbose_name='变量值')),
                ('latest_date', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '变量表',
                'db_table': 'variable_info',
            },
        ),
        migrations.AddField(
            model_name='connectioninfo',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connectioninfo',
            name='latest_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='inventorygroups',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-03-07', verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventorygroups',
            name='latest_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='inventoryhosts',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-03-07', verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventoryhosts',
            name='latest_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='variableinfo',
            name='groups',
            field=models.ManyToManyField(to='db.InventoryGroups', verbose_name='归属组'),
        ),
        migrations.AddField(
            model_name='variableinfo',
            name='hosts',
            field=models.ManyToManyField(to='db.InventoryHosts', verbose_name='归属主机'),
        ),
    ]
