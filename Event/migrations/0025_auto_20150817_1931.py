# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0024_auto_20150817_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boughtticket',
            old_name='Payment',
            new_name='payment',
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(19, 31, 7, 666786)),
        ),
    ]
