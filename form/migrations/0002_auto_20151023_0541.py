# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollno', models.CharField(max_length=9, verbose_name=b'Roll No')),
                ('name', models.CharField(max_length=25, verbose_name=b'Name')),
                ('Present_Branch', models.CharField(max_length=25, verbose_name=b'Present Branch', choices=[(b'AE B.Tech', b'AE B.Tech'), (b'CE B.Tech', b'CE B.Tech'), (b'CH', b'CH'), (b'CL B.Tech', b'CL B.Tech'), (b'CL Dual Deg', b'CL Dual Deg'), (b'CS B.Tech', b'CS B.Tech'), (b'EE B.Tech', b'EE B.Tech'), (b'EE Dual Deg E1', b'EE Dual Deg E1'), (b'EE Dual Deg E2', b'EE Dual Deg E2'), (b'EN Dual Deg', b'EN Dual Deg'), (b'EP B.Tech', b'EP B.Tech'), (b'EP Dual Deg N1', b'EP Dual Deg N1'), (b'ME B.Tech', b'ME B.Tech'), (b'ME Dual Deg M2', b'ME Dual Deg M2'), (b'MM B.Tech', b'MM B.Tech'), (b'MM Dual Deg Y1', b'MM Dual Deg Y1'), (b'MM Dual Deg Y2', b'MM Dual Deg Y2')])),
                ('Category', models.CharField(default=b'General', max_length=7, verbose_name=b'Category', choices=[(b'General', b'General'), (b'OBC', b'OBC'), (b'SC', b'SC'), (b'ST', b'ST')])),
                ('cpi', models.DecimalField(verbose_name=b'CPI', max_digits=2, decimal_places=2)),
                ('Preference_1', models.CharField(max_length=25, verbose_name=b'Preference 1', choices=[(b'AE B.Tech', b'AE B.Tech'), (b'CE B.Tech', b'CE B.Tech'), (b'CH', b'CH'), (b'CL B.Tech', b'CL B.Tech'), (b'CL Dual Deg', b'CL Dual Deg'), (b'CS B.Tech', b'CS B.Tech'), (b'EE B.Tech', b'EE B.Tech'), (b'EE Dual Deg E1', b'EE Dual Deg E1'), (b'EE Dual Deg E2', b'EE Dual Deg E2'), (b'EN Dual Deg', b'EN Dual Deg'), (b'EP B.Tech', b'EP B.Tech'), (b'EP Dual Deg N1', b'EP Dual Deg N1'), (b'ME B.Tech', b'ME B.Tech'), (b'ME Dual Deg M2', b'ME Dual Deg M2'), (b'MM B.Tech', b'MM B.Tech'), (b'MM Dual Deg Y1', b'MM Dual Deg Y1'), (b'MM Dual Deg Y2', b'MM Dual Deg Y2')])),
            ],
        ),
        migrations.DeleteModel(
            name='form',
        ),
    ]
