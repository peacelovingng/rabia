# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='contentTitle',
            new_name='content_title',
        ),
    ]
