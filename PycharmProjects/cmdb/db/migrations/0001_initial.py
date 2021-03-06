# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetChangLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='变更内容')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '资产变更日志表',
                'db_table': 'asset_change_log',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=8, verbose_name='插槽位')),
                ('model', models.CharField(max_length=32, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('pd_type', models.CharField(max_length=32, verbose_name='接口类型')),
            ],
            options={
                'verbose_name': '硬盘表',
                'verbose_name_plural': '硬盘表',
                'db_table': 'disk',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='容量')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存SN号')),
                ('speed', models.CharField(blank=True, max_length=16, null=True, verbose_name='速度')),
            ],
            options={
                'verbose_name': '内存表',
                'verbose_name_plural': '内存表',
                'db_table': 'memory',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='网卡名称')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('netmask', models.CharField(max_length=64, verbose_name='掩码')),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip地址')),
                ('up', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '网卡表',
                'verbose_name_plural': '网卡表',
                'db_table': 'nic',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=128, unique=True, verbose_name='主机名')),
                ('sn', models.CharField(db_index=True, max_length=64, verbose_name='SN号')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='型号')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('machine', models.CharField(blank=True, max_length=16, null=True, verbose_name='硬件平台')),
                ('os_name', models.CharField(blank=True, max_length=16, null=True, verbose_name='系统名称')),
                ('os_version', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统版本')),
                ('kernel', models.CharField(blank=True, max_length=128, null=True, verbose_name='内核信息')),
                ('model_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号')),
                ('cpu_type', models.CharField(blank=True, max_length=16, null=True, verbose_name='CPU 架构')),
                ('physical_count', models.IntegerField(blank=True, null=True, verbose_name='CPU物理个数')),
                ('physical_cores', models.IntegerField(blank=True, null=True, verbose_name='每颗 CPU 核心数')),
                ('processor_cores_count', models.IntegerField(blank=True, null=True, verbose_name='CPU 总逻辑核心数')),
                ('latest_date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '服务器表',
                'verbose_name_plural': '服务器表',
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='组名')),
            ],
            options={
                'verbose_name_plural': '用户组表',
                'db_table': 'user_group',
            },
        ),
        migrations.CreateModel(
            name='UsersProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
            ],
            options={
                'verbose_name_plural': '用户表',
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='db.UsersProfile', verbose_name='用户成员'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='db.Server', verbose_name='所属服务器'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='db.Server', verbose_name='所属服务器'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='db.Server', verbose_name='所属服务器'),
        ),
        migrations.AddField(
            model_name='assetchanglog',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.UsersProfile'),
        ),
        migrations.AddField(
            model_name='assetchanglog',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar', to='db.Server'),
        ),
    ]
