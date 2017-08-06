# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0125_auto_20170805_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='nomi_session',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018)], null=True),
        ),
        migrations.AlterField(
            model_name='posthistory',
            name='post_tenure',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018)], null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='tenure',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018)], default=2017, null=True),
        ),
    ]