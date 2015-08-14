# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0015_auto_20150814_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='num_of_raters',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='rate_sum',
            field=models.IntegerField(default=0),
        ),
    ]
