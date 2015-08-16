# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0021_auto_20150816_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sold',
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(15, 15, 33, 114687)),
        ),
    ]
