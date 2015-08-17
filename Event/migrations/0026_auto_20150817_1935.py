# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Event.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0025_auto_20150817_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(19, 35, 21, 435502), blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='code',
            field=models.CharField(default=Event.models.code_generate, max_length=20, unique=True),
        ),
    ]
