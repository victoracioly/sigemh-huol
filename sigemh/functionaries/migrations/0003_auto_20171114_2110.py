# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionaries', '0002_auto_20171114_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionary',
            options={'verbose_name': 'Funcinário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterField(
            model_name='functionary',
            name='name',
            field=models.CharField(max_length=75, verbose_name='Nome'),
        ),
    ]
