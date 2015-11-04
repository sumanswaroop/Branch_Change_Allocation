# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20151026_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, null=True, blank=True)),
                ('sancstrength_1', models.PositiveIntegerField()),
                ('sancstrength_2', models.PositiveIntegerField()),
                ('sancstrength_3', models.PositiveIntegerField()),
                ('sancstrength_4', models.PositiveIntegerField()),
                ('sancstrength_5', models.PositiveIntegerField()),
                ('sancstrength_6', models.PositiveIntegerField()),
                ('sancstrength_7', models.PositiveIntegerField()),
                ('sancstrength_8', models.PositiveIntegerField()),
                ('sancstrength_9', models.PositiveIntegerField()),
                ('sancstrength_10', models.PositiveIntegerField()),
                ('sancstrength_11', models.PositiveIntegerField()),
                ('sancstrength_12', models.PositiveIntegerField()),
                ('sancstrength_13', models.PositiveIntegerField()),
                ('sancstrength_14', models.PositiveIntegerField()),
                ('sancstrength_15', models.PositiveIntegerField()),
                ('sancstrength_16', models.PositiveIntegerField()),
                ('sancstrength_17', models.PositiveIntegerField()),
                ('currstrength_1', models.PositiveIntegerField()),
                ('currstrength_2', models.PositiveIntegerField()),
                ('currstrength_3', models.PositiveIntegerField()),
                ('currstrength_4', models.PositiveIntegerField()),
                ('currstrength_5', models.PositiveIntegerField()),
                ('currstrength_6', models.PositiveIntegerField()),
                ('currstrength_7', models.PositiveIntegerField()),
                ('currstrength_8', models.PositiveIntegerField()),
                ('currstrength_9', models.PositiveIntegerField()),
                ('currstrength_10', models.PositiveIntegerField()),
                ('currstrength_11', models.PositiveIntegerField()),
                ('currstrength_12', models.PositiveIntegerField()),
                ('currstrength_13', models.PositiveIntegerField()),
                ('currstrength_14', models.PositiveIntegerField()),
                ('currstrength_15', models.PositiveIntegerField()),
                ('currstrength_16', models.PositiveIntegerField()),
                ('currstrength_17', models.PositiveIntegerField()),
            ],
        ),
    ]
