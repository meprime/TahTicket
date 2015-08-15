# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0018_auto_20150813_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='Event.Type', default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(11, 51, 10, 261332)),
        ),
    ]
