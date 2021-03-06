# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('interval', models.IntegerField(default=300, verbose_name='告警间隔(s)')),
                ('recover_notice', models.BooleanField(default=True, verbose_name='故障恢复后发送通知消息')),
                ('recover_subject', models.CharField(blank=True, max_length=128, null=True)),
                ('recover_message', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('host_groups', models.ManyToManyField(blank=True, to='Monitor.HostGroup')),
                ('hosts', models.ManyToManyField(blank=True, to='Monitor.Host')),
            ],
        ),
        migrations.CreateModel(
            name='TriggerExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specified_index_key', models.CharField(blank=True, max_length=64, null=True, verbose_name='只监控专门指定的指标key')),
                ('operator_type', models.CharField(choices=[('eq', '='), ('lt', '<'), ('gt', '>')], max_length=32, verbose_name='运算符')),
                ('data_calc_func', models.CharField(choices=[('avg', 'Average'), ('max', 'Max'), ('hit', 'Hit'), ('last', 'Last')], max_length=64, verbose_name='数据处理方式')),
                ('data_calc_args', models.CharField(help_text='若是多个参数,则用,号分开,第一个值是时间', max_length=64, verbose_name='函数传入参数')),
                ('threshold', models.IntegerField(verbose_name='阈值')),
                ('logic_type', models.CharField(blank=True, choices=[('or', 'OR'), ('and', 'AND')], max_length=32, null=True, verbose_name='与一个条件的逻辑关系')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monitor.Service', verbose_name='关联服务')),
                ('service_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monitor.ServiceIndex', verbose_name='关联服务指标')),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monitor.Trigger', verbose_name='所属触发器')),
            ],
        ),
        migrations.AddField(
            model_name='actionoperation',
            name='msg_format',
            field=models.TextField(default='Host({hostname},{ip}) service({service_name}) has issue,msg:{msg}', verbose_name='消息格式'),
        ),
        migrations.AlterField(
            model_name='actionoperation',
            name='step',
            field=models.SmallIntegerField(default=1, verbose_name='第n次告警'),
        ),
        migrations.AddField(
            model_name='action',
            name='operations',
            field=models.ManyToManyField(to='Monitor.ActionOperation'),
        ),
        migrations.AddField(
            model_name='action',
            name='triggers',
            field=models.ManyToManyField(blank=True, help_text='想让哪些trigger触发当前报警动作', to='Monitor.Trigger'),
        ),
    ]
