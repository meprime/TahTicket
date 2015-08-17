# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0022_auto_20150816_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='boughtticket',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='boughtticket',
            name='payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(18, 9, 1, 591255), blank=True),
        ),
    ]
