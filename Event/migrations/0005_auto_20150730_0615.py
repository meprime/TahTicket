# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0004_auto_20150721_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='organizer',
        ),
        migrations.AlterField(
            model_name='boughtticket',
            name='buyer',
            field=models.ForeignKey(to='User.UserProfile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2015, 7, 30)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(1, 45, 19, 651795)),
        ),
    ]
