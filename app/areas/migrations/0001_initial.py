# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created date')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='last modified')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='catalogs.Catalog')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
