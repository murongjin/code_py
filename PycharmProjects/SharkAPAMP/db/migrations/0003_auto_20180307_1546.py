# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20180305_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_user', models.CharField(max_length=64, verbose_name='远程登录用户名')),
                ('password', models.CharField(max_length=255, verbose_name='登录密码')),
                ('port', models.IntegerField()),
                ('ssh_pub_key_path', models.CharField(blank=True, default='', max_length=255, verbose_name='公钥存储路径')),
                ('ssh_private_key_path', models.CharField(blank=True, default='', max_length=255, verbose_name='私钥存储路径')),
                ('host', models.ManyToManyField(null=True, to='db.Server', verbose_name='主机 ID')),
            ],
        ),
        migrations.AlterField(
            model_name='moduleinfo',
            name='module_lang',
            field=models.IntegerField(choices=[(0, '-------'), (1, 'python'), (2, 'shell'), (3, '其他')], verbose_name='开发语言'),
        ),
        migrations.AlterField(
            model_name='moduleinfo',
            name='module_type',
            field=models.IntegerField(choices=[(0, '-------'), (1, 'ansible'), (2, 'shell'), (3, 'salt')], verbose_name='模块类型'),
        ),
    ]