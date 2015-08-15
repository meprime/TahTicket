# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20150730_0615'),
        ('Event', '0019_auto_20150815_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='User.UserProfile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(8, 54, 25, 957221), blank=True),
        ),
    ]
