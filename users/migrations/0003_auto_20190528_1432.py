# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-05-28 06:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_employee_department'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='employees',
        ),
    ]
