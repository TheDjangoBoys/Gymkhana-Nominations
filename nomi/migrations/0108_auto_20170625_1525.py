# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0107_auto_20170625_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='club_nomi', to='nomi.Club'),
        ),
    ]