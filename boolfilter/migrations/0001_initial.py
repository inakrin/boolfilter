# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.BooleanField()),
                ('last', models.BooleanField()),
            ],
        ),
    ]
