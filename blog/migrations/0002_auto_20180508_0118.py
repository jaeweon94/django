# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-07 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도/경도 포맷으로 입력', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 입력해주세요. 최대 100자 내외', max_length=100, verbose_name='제목'),
        ),
    ]
