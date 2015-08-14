# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0013_auto_20150813_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='boughtticket',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2015, 8, 14)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(verbose_name=datetime.time(16, 7, 12, 443515)),
        ),
    ]
