# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-15 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrecord',
            name='commit',
            field=models.CharField(help_text='record commit', max_length=100, verbose_name='record commit'),
        ),
    ]