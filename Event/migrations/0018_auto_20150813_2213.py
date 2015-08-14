# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20150730_0615'),
        ('Event', '0017_auto_20150814_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketRate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='num_of_raters',
        ),
        migrations.RemoveField(
            model_name='event',
            name='rate_sum',
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(5, 13, 23, 112862)),
        ),
        migrations.AddField(
            model_name='ticketrate',
            name='event',
            field=models.ForeignKey(to='Event.Event'),
        ),
        migrations.AddField(
            model_name='ticketrate',
            name='user',
            field=models.ForeignKey(to='User.UserProfile'),
        ),
        migrations.AddField(
            model_name='event',
            name='rate',
            field=models.ManyToManyField(through='Event.TicketRate', to='User.UserProfile'),
        ),
    ]
