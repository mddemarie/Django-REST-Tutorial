# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='snippets',
            field=models.ManyToManyField(to='snippets.Snippet'),
        ),
    ]
