# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20151023_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='cpi',
            field=models.DecimalField(verbose_name=b'CPI', max_digits=5, decimal_places=2),
        ),
    ]
