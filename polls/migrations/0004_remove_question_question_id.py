# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170611_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
    ]
