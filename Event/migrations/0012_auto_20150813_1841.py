# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0011_auto_20150813_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtype',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
