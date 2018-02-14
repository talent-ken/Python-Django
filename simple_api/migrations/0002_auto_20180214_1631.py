# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 11:01
from __future__ import unicode_literals

from django.db import migrations
from datetime import datetime

def create_initial_list(apps, schema_editor):
    Todo = apps.get_model('simple_api', 'Todo')

    Todo(
        title='Do Django',
        description='Do something Django',
        is_active=True,
        created_at=datetime.now(),
        priority='H'
    ).save()

    Todo(
        title='Finish Django REST',
        description='Complete Django REST Framework',
        is_active=True,
        created_at=datetime.now(),
        priority='N'
    ).save()

    Todo(
        title='Revise everything',
        description='Test description',
        is_active=False,
        created_at=datetime.now(),
        priority='L'
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('simple_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_list),
    ]