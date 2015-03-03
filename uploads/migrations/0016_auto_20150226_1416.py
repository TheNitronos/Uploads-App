# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0015_auto_20150225_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='proprietaire',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
