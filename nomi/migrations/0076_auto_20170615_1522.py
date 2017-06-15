# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0075_auto_20170615_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='status',
            field=models.CharField(choices=[('Nomination created', 'Nomination created'), ('Nomination out', 'Nomination out'), ('Interview period', 'Interview period'), ('Result compiled', 'Result compiled'), ('Work done', 'Work done')], default='Nomination created', max_length=50),
        ),
    ]
