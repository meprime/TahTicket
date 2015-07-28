# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='M', choices=[('M', 'مرد'), ('F', 'زن')], max_length=1),
        ),
        migrations.AddField(
            model_name='customer',
            name='nl_memb',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(blank=True, null=True, max_length=11),
        ),
    ]
