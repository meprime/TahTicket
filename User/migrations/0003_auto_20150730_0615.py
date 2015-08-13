# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        #('Event', '0005_auto_20150730_0615'),
        ('User', '0002_auto_20150721_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('phone_no', models.CharField(blank=True, null=True, max_length=11)),
                ('gender', models.CharField(choices=[('M', 'مرد'), ('F', 'زن')], default='M', max_length=1)),
                ('nl_memb', models.BooleanField(default=False)),
                ('is_privileged', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='eventorganizer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='EventOrganizer',
        ),
    ]
