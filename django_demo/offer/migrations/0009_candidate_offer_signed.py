# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_auto_20160818_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='offer_signed',
            field=models.BooleanField(default=False),
        ),
    ]