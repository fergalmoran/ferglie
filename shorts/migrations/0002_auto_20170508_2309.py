# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortened_url',
            field=models.CharField(default='pQUtRO', max_length=6, unique=True),
        ),
    ]