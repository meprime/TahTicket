# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_auto_20150730_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date(2015, 8, 13)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(12, 39, 4, 509429)),
        ),
        migrations.AlterField(
            model_name='subtype',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
