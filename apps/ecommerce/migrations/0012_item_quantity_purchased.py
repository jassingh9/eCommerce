# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_auto_20170928_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity_purchased',
            field=models.IntegerField(null=True),
        ),
    ]
