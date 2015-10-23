# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20151023_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='Category',
            field=models.CharField(default='General', max_length=7, choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], verbose_name='Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpost',
            name='Preference_1',
            field=models.CharField(max_length=25, choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')], verbose_name='Preference 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpost',
            name='Present_Branch',
            field=models.CharField(max_length=25, choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')], verbose_name='Present Branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpost',
            name='cpi',
            field=models.DecimalField(verbose_name='CPI', max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpost',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpost',
            name='rollno',
            field=models.CharField(max_length=9, verbose_name='Roll No'),
            preserve_default=True,
        ),
    ]
