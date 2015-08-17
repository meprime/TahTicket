# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0023_auto_20150817_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.BigIntegerField(auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(19, 29, 14, 779893), blank=True),
        ),
        migrations.AddField(
            model_name='boughtticket',
            name='Payment',
            field=models.ForeignKey(null=True, to='Event.Payment', blank=True),
        ),
    ]
