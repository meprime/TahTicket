# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoughtTicket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('buyer', models.ForeignKey(to='User.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                ('organizer', models.ForeignKey(to='User.EventOrganizer')),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20)),
                ('event', models.ForeignKey(to='Event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='subtype',
            name='type',
            field=models.ForeignKey(to='Event.Type'),
        ),
        migrations.AddField(
            model_name='event',
            name='sub_type',
            field=models.ForeignKey(to='Event.SubType'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='Event.Type'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='Event.Venue'),
        ),
        migrations.AddField(
            model_name='boughtticket',
            name='ticket',
            field=models.ForeignKey(to='Event.Ticket'),
        ),
    ]
