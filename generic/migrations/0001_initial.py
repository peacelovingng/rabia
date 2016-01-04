# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=1000)),
                ('contentTitle', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('resume', models.FileField(blank=True, default=None, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'', verbose_name='Image')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='generic.HomePage')),
            ],
        ),
    ]