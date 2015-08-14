# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0014_auto_20150814_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
